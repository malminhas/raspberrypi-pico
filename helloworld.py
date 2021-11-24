# helloworld.py
# =============
#
# Simple example that illustrates how to draw to display
# "hello world" and interact with the buttons in
# non-interrupt mode to change the colour of the text.
#
# Display screen buffer 240 x 135 with (0,0) top left
#

import utime
import picodisplay as display

def setBackground(r, g, b):
    # Set the background to black.
    display.set_pen(0, 0, 0)              # Set a black pen
    display.clear()

def printHelloWorld(r=255, g=255, b=255, br=0, bg=0, bb=0, x=5, y=5):
    setBackground(br, bg, bb)
    display.set_led(r, g, b)               # Set LED to (r,g,b)
    display.set_pen(r, g, b)               # Set an (r,g,b) pen   
    display.text('Hello', x, y, 0, 7)      # Add text
    display.text('World', x, y+45, 240, 7) # Add text
    display.rectangle(5,100,50,120)
    display.circle(80,115,15)
    #display.character(90,120,106)
    display.update()                       # Push the pixels to the screen

print(dir(display))
print(dir(display.BUTTON_X))
# Initialise Picodisplay with a bytearray display buffer
WIDTH = display.get_width()
HEIGHT = display.get_height()
buf = bytearray(WIDTH * HEIGHT)
display.init(buf)
display.set_backlight(1.0)
printHelloWorld(255, 255, 0)               # yellow
while True:
    if display.is_pressed(display.BUTTON_X):
        printHelloWorld(255, 0, 0)         # red
    elif display.is_pressed(display.BUTTON_Y):
        printHelloWorld(0, 255, 0)         # green
    elif display.is_pressed(display.BUTTON_A):
        printHelloWorld(0, 0, 255)         # blue
    elif display.is_pressed(display.BUTTON_B):
        printHelloWorld(255, 255, 255)     # white
