# helloworld.py
# =============
#
# Basic exmaple that illustrates how to draw to display
# "hello world" and interact with the buttons to change
# the colour of the text.
#

import utime
import picodisplay as display

def setBackground(r, g, b):
    # Set the background to black.
    display.set_pen(0, 0, 0)              # Set a black pen
    display.clear()

def printHelloWorld(r=255, g=255, b=255, br=0, bg=0, bb=0, x=5, y=5):
    setBackground(br, bg, bb)
    display.set_pen(r, g, b)        # Set an (r,g,b) pen   
    display.text('Hello', x, y, 24, 7)   # Add some text
    display.text('Depop', x, y+45, 240, 7)   # Add some text
    display.update()                      # Push the pixels to the screen

# Initialise Picodisplay with a bytearray display buffer
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(1.0)
printHelloWorld(255, 0, 0)
while True:
    if display.is_pressed(display.BUTTON_X):
        printHelloWorld(255, 0, 0)
    elif display.is_pressed(display.BUTTON_Y):
        printHelloWorld(0, 255, 0)
    elif display.is_pressed(display.BUTTON_A):
        printHelloWorld(0, 0, 255)
    elif display.is_pressed(display.BUTTON_B):
        printHelloWorld(255, 255, 255)
