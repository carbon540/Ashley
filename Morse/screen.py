import busio
from digitalio import DigitalInOut
import board
# Import the SSD1306 module.
import adafruit_ssd1306

class Screen:
    def __init__(self):
        """
        Creates a connection with the 128x32 OLED display
        """
        # Create the I2C interface.
        i2c = busio.I2C(board.SCL, board.SDA)

        # 128x32 OLED Display
        reset_pin = DigitalInOut(board.D4)
        display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
        # Clear the display.
        display.fill(0)
        display.show()
        width = display.width
        height = display.height

    def disp(self, send_buffer, receive_buffer):
        """
        INPUTS:
        send_buffer - string of most recent signals sent, as . and -
        receive_buffer - string of most recent signals received
        """
        pass
        display.text(send_buffer, width-85, height-7, 1)
        display.text(receive_buffer, width-85, height-7, 2)
        display.show()