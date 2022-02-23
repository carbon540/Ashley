#main.py

import board
import busio
import digitalio
import adafruit_rfm9x
from datetime import datetime

# Set radio frequency, in MHz
# 915.0 for US, 868.0 for UK/Europe
RADIO_FREQ_MHZ = 868.0

# Set board pins
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)

# Initialise SPI connection to RFM95 module
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialise class
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# SETTINGS of transceiver. These can be altered to improve range or bitrate

# Power of transceiver. Max value is 23dB.
rfm9x.tx_power = 23

# Spreading factor. 
# Valid settings are (6, 7, 8, 9, 10, 11, 12)
# Higher settings improve range and decrease rate
rfm9x.spreading_factor = 12

# Signal bandwidth
# Valid settings are (7800, 10400, 15600, 20800, 31250, 41700, 62500, 125000, 250000)
# Higher values increase throughput
rfm9x.signal_bandwidth = 7800

# Coding rate
# Valid settings are (5, 6, 7, 8)
# Level of redundency - higher values are more interference-tolerant
rfm9x.coding_rate = 8

# Enable CRC (cyclic redundency checker)
# Valid settings are (True, False)
# Increases redundency
# rfm9x.enable_crc = True

def main():
    while True:
        if button.send() == True:
            radio.send()
        else:
            radio.receive()
        pause(1)

if __name__ == "main.py":
    main()