# Basic example of FeatherWing OLED Usage
# https://www.adafruit.com/product/2900
# This example and library is meant to work with Adafruit CircuitPython API.
# Author: Brent Rubell
# License: Public Domain

# Import all board pins.
from board import SCL, SDA, D9, D6, D5
import busio
import digitalio


# Import the SSD1306 module.
import adafruit_ssd1306

# OLED FeatherWing Buttons
button_a = digitalio.DigitalIn(D9)
button_b = digitalio.DigitalIn(D6)
button_c = digitalio.DigitalIn(D5)

button_a.switch_to_input(pull=digitalio.Pull.Up)
button_b.switch_to_input(pull=digitalio.Pull.Up)
button_c.switch_to_input(pull=digitalio.Pull.Up)

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()


while True:
    display.text('Button', 0, 0)
    if button_a.value:
        display.text('A', 0, 10)
    elif button_b.value:
        display.text('B', 0, 10)
    elif button_c.value:
        display.text('C', 0, 10)
    else:
        display.text('None', 0, 10)
    # Clear the Display
    display.fill(0)
    display.show()
