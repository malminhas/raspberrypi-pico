# Raspberry Pi Pico

## Basic setup
* Microcontroller development boards
* RP2040 microcontroller
* Useful for IoT projects
* Need to solder the header pins on
* Accessible via Micropython or C/C++
* Installation of Micropython involves clicking on Index.htm file then downloading .uf2 file
* Thonny IDE for Micropython
* Can also use CLI.  Mac setup instructions are here:
* https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf 
* You communicate with Pico using minicom:
$ brew install minicom
$ minicom -b 115200 -o -D /dev/tty.usbmodem0000000000001
* Here’s how to flash the onboard LED:
```
>>> from machine import Pin 
>>> led = Pin(25, Pin.OUT)
>>> led.value(1)
>>> while True:
...     led.value(1)
...     time.sleep(0.5)
...     led.value(0)
...     time.sleep(0.5)
<ENTER>
```
* Thonny download from here: https://thonny.org/ 
* Can save code locally or on Pico

## GPIO
* A GPIO pin supports only two states, high and low
* An ADC pin supports a range of values, which is determined by the input voltage applied to the pin
* 12 bit ADC built into RP2040 microcontroller
* Three channels via GP26_ADC0, GP26_ADC1, GP28_ADC2 
* Fourth channel is built-in temperature sensor on 
```
from machine import Pin, Timer
import utime

red_led = Pin(12, Pin.OUT)
amber_led = Pin(15, Pin.OUT)
green_led = Pin(14, Pin.OUT)
builtin_led = Pin(25, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

def cycle_lights(green,amber,red,t):
    builtin_led.value(0)
    green_led.value(0)
    amber_led.value(0)
    red_led.value(0)
    green and green_led.value(1) 
    amber and amber_led.value(1)
    red and red_led.value(1)
    utime.sleep(t)

def flash_lights(green,amber,red,t):    
    green_led.value(green)
    amber_led.value(amber)
    red_led.value(red)
    utime.sleep(t)
    
def on_pressed(timer):
    print(button.value())
    assert(button.value() == 1)
    builtin_led(1)
    flash_lights(1,1,1,0.1)
    flash_lights(0,0,0,0.1)
    flash_lights(1,1,1,0.1)
    flash_lights(0,0,0,0.1)
    red_led.value(1)
    utime.sleep(5)
    flash_lights(1,1,1,0.1)
    flash_lights(0,0,0,0.1)
    flash_lights(1,1,1,0.1)
    flash_lights(0,0,0,0.1)    
    builtin_led(0)
    
# We just cycle through the traffic lights until interrupted
button.irq(trigger=Pin.IRQ_RISING, handler=on_pressed)
while True:
    cycle_lights(1,0,0,2)
    cycle_lights(0,1,0,1)
    cycle_lights(0,0,1,2)
    cycle_lights(0,1,0,1)
```

## Pimoroni Display
* https://shop.pimoroni.com/products/pico-display-pack
* 18-bit capable 240x135 pixel IPS display
* You need to install Pimoroni’s firmware  following the instructions here: https://github.com/UnfinishedStuff/Pimoroni_Pico_Display_Pack_documentation#quickstart-script 
* Note that when the LiPo shim is in place it must be switched ON for Thonny to detect the pico
* Same applies when trying to flash a pico with a LiPo shim soldered in place
* With the latest Pimoroni firmware you can use Thonny with the pico live.

## RFID reader
* Install vanilla micropython image on your pico
* git clone the repo here: https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion
* Connect via Thonny and copy three files from lib over to pico
* Run board_test.py

## C/C++
* SDK details here: https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf 
* SDK: https://github.com/raspberrypi/pico-sdk 
* Examples: https://github.com/raspberrypi/pico-examples 
* Extras: https://github.com/raspberrypi/pico-extras 
* Playground: https://github.com/raspberrypi/pico-playground 

