import board
import busio
import digitalio
import adafruit_rfm9x
from datetime import datetime as dt
import time

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
rfm9x.enable_crc = True

def wrt(message) -> None:
    """
    Opens a CSV file, writes a message, closes
    Prints to terminal
    """
    with open("/home/pi/Ashley/Practice/sendlog.csv",'w') as log:
        log.write(message)
        print(message)
        
try:
    while True:
        packet_text = "Hello world!\r\n"
        packet = bytes(packet_text, "utf-8")
        tm = str(dt.now())
        rfm9x.send(packet)
        time.sleep(1)  
        
        message = "{0}, Transmitted, {1}, {2}".format(tm, packet, packet_text)
        
        wrt(message)
except KeyboardInterrupt:
    print('Transmission loop ended')
