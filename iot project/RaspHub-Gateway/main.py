import digitalio
import board
import busio
import adafruit_rfm9x as LoRa

# LoRa - https://github.com/KevinLindemark/lora_esp32_rfm9x
RADIO_FREQ_MHZ = 433.0
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Lora Radio
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)

while True:
    # Modtag data fra LoRa og så bliver den gemt i received_data
    received_data = LoRa.receive()
    
    # Hvis der er modtaget data og det ikke er ingenting
    if received_data is not None:
        # Så konvertere den dataen = streng 
        received_string = str(received_data, "utf-8")
        print(received_string)
