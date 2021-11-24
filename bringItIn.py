# bringItIn.py
# ============
#
# pomodoro timer
#
# Mal Minhas <mal@malm.co.uk>
# v0.1 11.04.21
# v0.2 13.04.21
# v0.3 18.11.21
#

import utime
import picodisplay as display
from machine import PWM, Pin

# IMPORTANT: Can't use GPIO 12,13,14,15 as it interferes with Pico Display buttons :-/
GPOUT = 10
START_X = 0
START_Y = 0
# Get the width of the display, in pixels
WIDTH = display.get_width()
# Get the height of the display, in pixels
HEIGHT = display.get_height()

def initDisplay(brightness=0.5):
    # Initialise Picodisplay with a bytearray display buffer
    buf = bytearray(WIDTH * HEIGHT * 2)
    display.init(buf)
    display.set_backlight(brightness)

def setPen(color):
    if color == 'black':
        display.set_pen(0, 0, 0)       # Set a black pen
    elif color == 'white':
        display.set_pen(255, 255, 255) # Set a white pen
    elif color == 'red':
        display.set_pen(255, 0, 0)     # Set a red pen
    elif color == 'green':
        display.set_pen(0, 255, 0)     # Set a green pen
        
def setBackground(color='black'):
    setPen(color)                      # Set the background color
    display.clear()                    # Clear the display buffer

def goLive():
    print('Go live')
    display.set_led(0,255,0)             # Set the LED to green
    setBackground('black')
    ts = '00:00'
    setPen('red')                        # Set the text color
    display.text('LIVE', 50, 44, 240, 7) # Add some text
    display.text(ts, 50, 94, 240, 3)     # Add some text
    display.update()                     # Push the pixels to the screen
    goBeep(4000)

def goBeep(freq):
    print('beep')
    level = 1000
    buzzer = PWM(Pin(GPOUT))
    buzzer.freq(freq)
    buzzer.duty_u16(level)
    utime.sleep(0.5)
    buzzer.duty_u16(0)
            
initDisplay(brightness=1.0)
running = True
state = 'idle'
x = START_X
y = START_Y
xinc = 1
yinc = 1
t0 = None
backgroundColor = 'black'
textColor = 'red'
setBackground(backgroundColor)
while running:
    if state == 'idle':
        setPen(textColor)                             # Set the text color
        display.text('Depop', x, y, 240, 7)       # Add some text
        display.text('Sellers!', x+2, y+50, 240, 5)       # Add some text
        display.text("bring it in!", x+4, y+95, 240, 3) # Add some text
        display.update()                         # Push the pixels to the screen
        #if display.is_pressed(display.BUTTON_X): # X pressed
        #    print("X pressed!")
        #    running = False
        if display.is_pressed(display.BUTTON_X): # Y pressed
            print("X pressed!")
        if display.is_pressed(display.BUTTON_A): # Invert colours
            print("A pressed!")
            textColor = 'black'
            backgroundColor = 'red'
        if display.is_pressed(display.BUTTON_B): # Invert colours back
            textColor = 'red'
            backgroundColor = 'black'
        if display.is_pressed(display.BUTTON_Y): # Going live!
            state = 'goingLive'
        x += xinc
        y += yinc
        utime.sleep_ms(1)   # 1ms delay makes it nice and smooth.
        if x > 47:
            xinc = -1
        elif x == -3:
            xinc = 1
        if y > 22:
            yinc = -1
        elif y == -10:
            yinc = 1
        setBackground(backgroundColor)
    elif state == 'goingLive':
        goLive()
        t0 = utime.time()
        state = 'live'
    elif state == 'live':
        t = utime.time() - t0
        mins = t // 60
        secs = t % 60
        timestamp = str("%02d:%02d" % (mins,secs))
        print(timestamp)
        try:
            setBackground('black')
            setPen('green')                          # Set the text color
            display.text(timestamp, 40, 30, 240, 7)  # The ticking clock
            display.text('LIVE', 40, 80, 240, 3)     # The smaller 'LIVE' banner
            display.update()                         # Push the pixels to the screen
        except TypeError as e:
            # Very occasionally/randomly you get this exception raised by display.text(timestamp,...)
            # TypeError: Can't convert 'int' object to str implicitly
            # This code is attempts to capture it
            # Eventually after a few loops, things normally recover
            print("exception!")
            print(e)
            print(t0)
            t = utime.time() - t0
            mins = t // 60
            secs = t % 60
            timestamp = str("%02d:%02d" % (mins,secs))
            print(mins)
            print(secs)
            print(type(timestamp))
            print(timestamp)
            print('---------------')
        finally:
            pass
        # Check for keypress of X every 10ms to break us out of loop.
        # This would be more elegant if we had irq support on the display buttons.
        for i in range(100):
            utime.sleep_ms(10)
            if display.is_pressed(display.BUTTON_X):
                print('Go idle')
                setBackground(backgroundColor)
                display.set_led(0,0,0)             # Set the LED to black
                state = 'idle'
                goBeep(3000)
                break

print("Exited")
