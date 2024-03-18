import digitalio
import board
import busio
import adafruit_rfm9x as LoRa
import paho.mqtt.publish as publish

RADIO_FREQ_MHZ = 433.0
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)

while True:
    received_data = LoRa.receive()
    if received_data is not None:
        # Så konvertere den dataen = streng 
        received_string = str(received_data, "utf-8")
        print(received_string)
        publish.single("sg5-2a", received_string, hostname="mqtt.eclipseprojects.io")

