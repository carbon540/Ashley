import board
import busio
import digitalio
import adafruit_rfm9x
from datetime import datetime
import time
from alphabet import morseAlphabet
import screen
import buffer

send_buffer = buffer()
receive_buffer = buffer()
GPIO_DOT = 5
GPIO_DASH = 6

if __name__ =='__main__':
    raise NotImplementedError()
    # 1.0 start listening for new packets
        # 1.1 run check on previous 8 characters stored in buffer
        # 1.2 write new characters to display
    screen.disp(send_buffer, receive_buffer)
    # 2.0 send packets