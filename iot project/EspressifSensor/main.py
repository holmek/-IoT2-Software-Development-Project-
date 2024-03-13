import dht
import machine
from machine import Pin
from machine import I2C
from machine import SPI
from time import sleep
import mpu6050
from mq135 import MQ135
import uasyncio as asyncio
from micropython_rfm9x import RFM9x as LoRa


# DHT11 - https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
digital_humidity_and_temperature_sensor = dht.DHT11(Pin(14))

# MPU-6050 - https://microcontrollerslab.com/micropython-mpu-6050-esp32-esp8266/
i2c_interface = I2C(scl=Pin(22), sda=Pin(21)) 
accelerometer = mpu6050.accel(i2c_interface)

# https://github.com/rubfi/MQ135/tree/master
air_quality_sensor = MQ135(0)

# LoRa - https://github.com/KevinLindemark/lora_esp32_rfm9x
RESET = Pin(14, Pin.OUT)
spi = SPI(2, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
CS = Pin(5, Pin.OUT)
RADIO_FREQ_MHZ = 868.0
rfm9x = RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

async def get_sensor_data():
    # Dette er dht11 og MQ135 data som bliver indsamlet
    digital_humidity_and_temperature_sensor.measure()
    temperature = digital_humidity_and_temperature_sensor.temperature()
    humidity = digital_humidity_and_temperature_sensor.humidity()
    corrected_ppm = air_quality_sensor.get_corrected_ppm(temperature, humidity)

    # Dette er batteri data som bliver indsamlet
    percentage = int(((sum(voltage_divider.read() for _ in range(120)) / 120) - 800) / 10.6)
    
    # Dette er MPU-6050 fald data som bliver indsamlet
    acceleration_z = accelerometer.get_values()["AcZ"]
    if acceleration_z < -5000:
        gyro_data = "device fall detected"
    else:
        gyro_data = "no fall detected"
        
    # Dette er variablen sensor_data som indeholder overnævnte datapunkter med lora hvert 1 minut
    sensor_data = f"SG52A Temperature: {temperature}, Humidity: {humidity}, Gyro: {gyro_data}, Air Quality: {corrected_ppm}, Battery: {percentage}"
    LoRa.send(bytes(sensor_data, "utf-8"))
    await asyncio.sleep(60)  
        
async def main():
    await get_sensor_data()
    
asyncio.run(main())
