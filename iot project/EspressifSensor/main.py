import dht
import machine
from machine import Pin, SoftI2C, SoftSPI, ADC
from time import sleep
import mpu6050
from mq135 import MQ135
import uasyncio as asyncio
from micropython_rfm9x import RFM9x

voltage_divider = ADC(Pin(34))
voltage_divider.atten(ADC.ATTN_11DB)
digital_humidity_and_temperature_sensor = dht.DHT11(Pin(25))
i2c_interface = SoftI2C(scl=Pin(22), sda=Pin(21))
accelerometer = mpu6050.accel(i2c_interface)
air_quality_sensor = MQ135(32)
RESET = Pin(14, Pin.OUT)
CS = Pin(5, Pin.OUT)
spi = SoftSPI(baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
RADIO_FREQ_MHZ = 868.0
rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

async def get_sensor_data():
    digital_humidity_and_temperature_sensor.measure()
    device_temperature = digital_humidity_and_temperature_sensor.temperature()
    device_humidity = digital_humidity_and_temperature_sensor.humidity()
    device_air_quality = int(air_quality_sensor.get_corrected_ppm(device_temperature, device_humidity))
    device_percentage = int(((sum(voltage_divider.read() for _ in range(120)) / 120) - 800) / 10.6)
    device_orientation = 1 if accelerometer.get_values()["AcZ"] > 3 - 12000 else 0
    device_orientation = 1 if accelerometer.get_values()["AcZ"] < -12000 or accelerometer.get_values()["AcZ"] > 12000 else 0
    sensor_data_message = f"{device_temperature}, {device_humidity}, {device_air_quality}, {device_percentage}, {device_orientation}, {device_detection}"
    rfm9x.send(bytes(sensor_data_message, "utf-8"))
    await asyncio.sleep(10)

async def main():
    while True:
        await get_sensor_data()

asyncio.run(main())
