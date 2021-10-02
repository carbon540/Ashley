# receive.py

import board
import busio
import digitalio
import adafruit_rfm9x

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

while True:
    packet = rfm9x.receive(timeout=1.0)
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        # Packet has not been received
        print("Null")
    else:
        # Packet received
        # Print out the raw bytes of the packet, the decoded ASCII and the signal strength
        # Make sure it is being sent in ASCII!
        packet_text = str(packet, "ascii")
        rssi = rfm9x.last_rssi
        print("Received, {0}, {1}, {2}".format(packet, packet_text, rssi))