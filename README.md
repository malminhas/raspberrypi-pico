# Raspberry Pi Pico

## Introduction
The Raspberry Pi Pico is a $4 microcontroller board released in January 2021 built around the [Raspberry Pi RP2040 microprocessor chip](https://www.raspberrypi.com/products/raspberry-pi-pico/):

> Designed by Raspberry Pi, RP2040 features a dual-core Arm Cortex-M0+ processor with 264KB internal RAM and support for up to 16MB of off-chip Flash. A wide range of flexible I/O options includes I2C, SPI, and — uniquely — Programmable I/O (PIO). These support endless possible applications for this small and affordable package

The Raspberry Pi Pico can be programmed using either C++ or MicroPython.  The latter is recommended for familiarisation purposes: 

> MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

> MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.

<img src="https://user-images.githubusercontent.com/12896870/144333163-72cc7bda-c286-42b2-b9f1-2f592c1003ec.png" height=400></img>

## Getting started
You can purchase Raspberry either with or without the header pins soldered.   You need to connect it to your laptop via microUSB while holding down the BOOTSEL button.  It will mount as a Mass Storage Device called RPI-RP2.  At that point you can drag and drop a MicroPython .uf2 image onto it.  Full instructions for installing basic MicroPython are [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython).  However if you are using the Pimoroni screen or wireless board as will be the case with the examples here then you want the .uf2 file from Pimoroni [here](
https://github.com/pimoroni/pimoroni-pico/releases).  Install the [Thonny IDE](https://thonny.org/) for Micropython.  Once you have Thonny installed you can communicate with the Raspberry Pi Pico using the Stop/Restart Backend button.  More details on how to address Pico from MicroPython are available in the comprehensive [here](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).
It is also possible to communicate with Pico via a CLI using minicom:
```
$ brew install minicom
$ minicom -b 115200 -o -D /dev/tty.usbmodem0000000000001
```
Here’s how to flash the onboard LED:
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
You can save code locally or on Pico.  If you copy and save a file onto Pico using Thonny as `main.py` it will launch on boot.

## Helloworld
Two versions of helloworld in MicroPython are included in this repo.  The basic version [`helloworld.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/helloworld.py) uses a loop to check `display.is_pressed`.  The other version [`helloworldirq.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/helloworldIrq.py) uses IRQ interrupt handlers to pick up the button presses on pull up which are on pins 12,13,14,15.

## Pico Timer
[`bringItIn.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/bringItIn.py) is a pomodoro timer in MicroPython with a floating screensaver.  You can invert the display by toggling between buttons B and A.  You trigger the timer by clicking the Y button and then exit back to screensaver by clicking X.

<a href="https://youtu.be/h-EeKiQ1Ww8"><img src="https://user-images.githubusercontent.com/12896870/144336860-74f29e23-a409-4abb-972d-610b2f2aafa5.png" width="500"/></a>

## GPIO
Some notes on GPIO operation:
* A GPIO pin supports only two states, high and low
* An ADC pin supports a range of values, which is determined by the input voltage applied to the pin
* 12 bit ADC built into RP2040 microcontroller
* Three channels are available via GP26_ADC0, GP26_ADC1, GP28_ADC2 
* A fourth channel is a built-in temperature sensor
* The following code will cycle through three LEDs connected to GPIO pins 12, 14 and 15. A button interrupt handler 
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

## Pimoroni Display Pack
Pimoroni have a 18-bit capable 240x135 pixel IPS display detailed [here](https://shop.pimoroni.com/products/pico-display-pack) addressable via MicroPython using the Pimoroni uf2 firmware image.  To access it you will need to install Pimoroni’s firmware following the instructions [here](https://github.com/UnfinishedStuff/Pimoroni_Pico_Display_Pack_documentation#quickstart-script).  If you are powering it via a LiPo shim, it must be switched ON for Thonny to detect the Pico.  The same applies when trying to flash a pico with a LiPo shim soldered in place.  With the latest Pimoroni firmware you can use Thonny with the pico live.

## Pimoroni Network Pack
Pimoroni have a WiFi network pack for Pico available [here](https://shop.pimoroni.com/products/pico-wireless-pack) addressable via MicroPython using the Pimoroni uf2 image.  The following code will 
```
import picowireless
import time

picowireless.init()
picowireless.start_scan_networks()
while True:
    networks = picowireless.get_scan_networks()
    print("Found {} network(s)...".format(networks))
    for network in range(networks):
        ssid = picowireless.get_ssid_networks(network)
        print("{}: {}".format(network, ssid))
    print("\n")
    time.sleep(10)
```

## RFID reader
Instructions for how to use:
* Install vanilla micropython image on your pico
* git clone the repo [here](https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion)
* Connect via Thonny and copy three files from lib over to pico
* Run board_test.py

## C/C++
Some notes:
* Getting started details [here](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf)
* [SDK](https://github.com/raspberrypi/pico-sdk)
* [Examples](https://github.com/raspberrypi/pico-examples) 
* [Extras](https://github.com/raspberrypi/pico-extras)
* [Playground](https://github.com/raspberrypi/pico-playground)
