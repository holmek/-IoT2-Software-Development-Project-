import digitalio
import board
import busio
import adafruit_rfm9x
from time import sleep
import paho.mqtt.publish as publish

RADIO_FREQ_MHZ = 868.0
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)

while True:
    received_data = rfm9x.receive()
    if received_data is not None:
        received_string = str(received_data, "utf-8")
        publish.single("sg5-2a", received_string, hostname="mqtt.eclipseprojects.io")
