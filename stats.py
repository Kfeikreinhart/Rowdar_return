# Created by: Michael Klements
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit Blinka & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
import time
import board
import busio
import gpiozero

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Use gpiozero to control the reset pin
oled_reset_pin = gpiozero.OutputDevice(4, active_high=False)  # GPIO 4 for reset, active low

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# Use I2C for communication
i2c = board.I2C()

# Manually reset the display (high -> low -> high for reset pulse)
oled_reset_pin.on()
time.sleep(0.1)  # Delay for a brief moment
oled_reset_pin.off()  # Toggle reset pin low
time.sleep(0.1)  # Wait for reset
oled_reset_pin.on()  # Turn reset pin back high

# Create the OLED display object
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear the display
oled.fill(0)
oled.show()

# Create a blank image for drawing
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)

while True:
    # Clear screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Custom message
    custom_message = "Hello from Pi!"  # <- change this to whatever message you want
    draw.text((0, 24), custom_message, font=font, fill=255)  # Center vertically

    # Display the image
    oled.image(image)
    oled.show()

    # Refresh delay
    time.sleep(LOOPTIME)
