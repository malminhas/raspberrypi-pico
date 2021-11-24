# helloworldIrq.py
# ================
#
# Simple example that illustrates how to draw to display "hello world" and interact 
# with the buttons using interrupt handling to change the colour of the text.
# Note how interrupts allow clean support for background hue increment support. 
#
# Display screen buffer 240 x 135 with (0,0) top left
#

import utime
import picodisplay as display

br,bg,bb = 0,0,0
r,g,b = 255,255,0

def setBackground(br, bg, bb):
    # Set the background to black.
    display.set_pen(br, bg, bb)              # Set a black pen
    display.clear()

def printHelloWorld(fr=255, fg=255, fb=255, br=0, bg=0, bb=0, x=5, y=5):
    setBackground(br, bg, bb)
    display.set_led(fr, fg, fb)            # Set LED to (r,g,b)
    display.set_pen(fr, fg, fb)            # Set an (r,g,b) pen   
    display.text('Hello', x, y, 0, 7)      # Add text
    display.text('World', x, y+45, 240, 7) # Add text
    display.rectangle(5,100,50,120)
    display.circle(80,115,15)
    #display.character(90,120,106)
    display.update()                       # Push the pixels to the screen

def A_task(pin):
    global r,g,b,br,bg,bb
    br,bg,bb,r,g,b = 0,0,0,255,255,255
    printHelloWorld(r, g, b)     # white
    A_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=A_task)

def B_task(pin):
    global r,g,b,br,bg,bb
    br,bg,bb,r,g,b = 0,0,0,255,0,0
    printHelloWorld(r, g, b)         # red
    B_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=B_task)

def X_task(pin):
    global r,g,b,br,bg,bb
    br,bg,bb,r,g,b = 0,0,0,0,255,0
    printHelloWorld(r, g, b)         # green
    X_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=X_task)

def Y_task(pin):
    global r,g,b,br,bg,bb
    br,bg,bb,r,g,b = 0,0,0,0,0,255
    printHelloWorld(r, g, b)         # blue
    Y_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=Y_task)

print(dir(display))
print(dir(display.BUTTON_X))
A_pin = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
A_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=A_task)
B_pin = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
B_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=B_task)
X_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
X_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=X_task)
Y_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
Y_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=Y_task)

# Initialise Picodisplay with a bytearray display buffer
WIDTH = display.get_width()
HEIGHT = display.get_height()
buf = bytearray(WIDTH * HEIGHT)
display.init(buf)
display.set_backlight(1.0)
printHelloWorld(r, g, b)               # yellow
while True:
    hueIncrement = 1
    utime.sleep_us(100)
    br = (br + hueIncrement) % 255
    bg = (bg + hueIncrement) % 255
    bb = (bb + hueIncrement) % 255
    printHelloWorld(r, g, b, br, bg, bb)
