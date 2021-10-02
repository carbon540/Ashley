import board
import busio
import digitalio
import adafruit_rfm9x
from datetime.datetime import now

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

# Set power of transceiver. Max value is 23dB.
rfm9x.tx_power = 23

def wrt(message) -> None:
    """
    Opens a CSV file, writes a message, closes
    Prints to terminal
    """
    with open("sendlog.csv") as log:
        log.write(message)
        print(message)
        
try:
    while True:
        #TODO: write transmission code
        
        wrt(message)
except KeyboardInterrupt:
    print('Transmission loop ended')
