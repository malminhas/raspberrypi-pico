# Raspberry Pi Pico Experiments
This repo contains various hacks and experiments with the Raspberry Pi Pico microcontroller focussed around a Pico Display Unit that was built as a standalone piece of hardware for running Pico software.  The next section outlines how this unit was built and the main scripts run on it.  The remainder of the README contains brief notes on getting started with the Pico with MicroPython, some nice peripherals for using with it and also how to build and run C/C++ code on the Pico.

## Pico Display Unit Examples
A Pico Display Unit is a standalone piece of kit built by soldering a LiPo shim to the header pins on the underside of a Pico then connecting a LiPo battery before plugging a Pimoroni Display Pack onto the header set.  The battery can be attached to the board using blutack as shown in the photos below in standalone form.  The LiPo shim is able to support charging the battery when a microUSB is attached.  The total cost for building one of these is £32.40 at time of writing in December 2021. 
|Showing front top|Showing front side|
:----------------:|:------------------:
| <img src="https://user-images.githubusercontent.com/12896870/144763531-ad4c9f62-239f-4f30-9f47-96b49e65c25b.png" alt="Pico Display Unit" width="350"/> |<img src="https://user-images.githubusercontent.com/12896870/144763558-d9c33266-193e-47a5-920d-4cce0194b174.png" alt="Pico Display Unit" width="515"/> |

The full list of parts needed to build one is contained in the following table. You will additionally need a soldering iron, solder and a USB-C to microUSB cable to connect your Mac to your unit.

| Item | Price | Comments | 
:----------------:|:----------------:|:----------------:
| Raspberry Pi Pico board only | £3.60 | :slightly_smiling_face: |
| Pico Stacking headers | £1.50 | If you buy a vanilla Pico, you will need to buy these and solder them to the board |
| LiPo shim | £6.90 | Convenient way of powering your Raspberry Pi Pico from a LiPo/LiIon battery. | 
| Pico Display Pack | £13.50 | A lovely 1.14" IPS LCD screen for Pico, with four useful buttons and a RGB LED |
| LiPo battery | £6.90 | Standard 3.7V 500mA standard battery used in drones |

### Helloworld
Two versions of helloworld in MicroPython are available.  The basic version [`helloworld.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/helloworld.py) uses a loop to check `display.is_pressed`.  The other version [`helloworldirq.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/helloworldIrq.py) uses IRQ interrupt handlers to pick up the button presses on pull up which are on pins 12,13,14,15.  In both scripts, pressing the buttons changes the colour of the display text.  Here are a couple of photos of [`helloworld.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/helloworld.py):

| Hello | World |
:----------------:|:----------------:
| <img src="https://user-images.githubusercontent.com/12896870/144760444-490463d5-9612-4116-a691-cffe8ede9c78.png" alt="voice tree" width="378"/> | <img src="https://user-images.githubusercontent.com/12896870/144760405-8d203a66-034e-4d40-b52b-078437cd278b.png" alt="voice tree" width="487"/> |

### Pico Timer
[`bringItIn.py`](https://github.com/malminhas/raspberrypi-pico/blob/main/bringItIn.py) is a pomodoro timer in MicroPython designed to run on the Pico Display Unit.  In default mode it shows a floating screensaver.  You can invert the display by toggling between buttons B and A.  You trigger the timer by clicking the Y button and then exit back to screensaver by clicking X.  The following image links to a video showing it in operation: 

<a href="https://youtu.be/h-EeKiQ1Ww8"><img src="https://user-images.githubusercontent.com/12896870/144336860-74f29e23-a409-4abb-972d-610b2f2aafa5.png" width="500"/></a>

## Introduction to the Raspberry Pi Pico
The Raspberry Pi Pico is a $4 microcontroller board released in January 2021 built around the [Raspberry Pi RP2040 microprocessor chip](https://www.raspberrypi.com/products/raspberry-pi-pico/):

> Designed by Raspberry Pi, RP2040 features a dual-core Arm Cortex-M0+ processor with 264KB internal on-chip SRAM and 2MB of off-chip Flash (extensible to 16MB). A wide range of flexible I/O options includes I2C, SPI, and — uniquely — Programmable I/O (PIO). These support endless possible applications for this small and affordable package. 

The Raspberry Pi Pico can be programmed using either C++ or MicroPython.  The latter is a recommended starting point for familiarisation purposes: 

> MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

> MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.

<img src="https://user-images.githubusercontent.com/12896870/144763868-de6d30fd-3e45-43fd-b198-6f024365942b.png" height=400></img>

## Getting started with MicroPython
You can purchase a Raspberry Pi Pico either with or without the header pins soldered.  In order to use it, you first need to load MicroPython firmware.  To do this connect it to your laptop via microUSB while holding down the BOOTSEL button.  It will mount as a Mass Storage Device called RPI-RP2.  At that point you can drag and drop a MicroPython .uf2 image onto it.  Full instructions for installing basic MicroPython are [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython).  If you are using the Pimoroni screen or wireless board as will be the case with the examples above then you want the .uf2 file from Pimoroni [here](
https://github.com/pimoroni/pimoroni-pico/releases).  Install the [Thonny IDE](https://thonny.org/) for Micropython.  Once you have Thonny installed you can communicate with the Raspberry Pi Pico using the Stop/Restart Backend button.  

<img src="https://user-images.githubusercontent.com/12896870/144759371-058f1460-a6ee-4556-8a74-15a60e9b5178.png" width=1210></img>

More details on how to address Pico from MicroPython are available in the comprehensive [here](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).  It is also possible to communicate with Pico via a CLI using `minicom`.  Note that the specific tty enumeration here is likely to be different in your local context:
```
$ brew install minicom
$ minicom -b 115200 -o -D /dev/tty.usbmodem14301
```
On my Mac I had to do ESC-Q to exist.  This MicroPython code will to flash the onboard LED:
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

## Pico GPIO
The Raspberry Pi Pico has programmable General Pupose I/O (GPIO) support.  More details on the pinout is available [here](https://www.raspberrypi-spy.co.uk/2021/01/pi-pico-pinout-and-power-pins/). Some notes on GPIO operation:
* A GPIO pin supports only two states, high and low
* An ADC pin supports a range of values, which is determined by the input voltage applied to the pin
* 12 bit ADC built into RP2040 microcontroller
* Three channels are available via GP26_ADC0, GP26_ADC1, GP28_ADC2 
* A fourth channel is a built-in temperature sensor
* The following MicroPython code will cycle through three LEDs connected to GPIO pins 12, 14 and 15 with 330 Ohm resistors per the image below. A button press interrupts the sequence.  

<img src="https://user-images.githubusercontent.com/12896870/144338383-cac2ba53-0776-4541-91f6-a000f5162e43.png" width=500></a>

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
Pimoroni sell a 18-bit capable 240x135 pixel IPS display detailed [here](https://shop.pimoroni.com/products/pico-display-pack) which is addressable via MicroPython using the Pimoroni uf2 firmware image.  To access it you will need to install Pimoroni’s firmware following the instructions [here](https://github.com/UnfinishedStuff/Pimoroni_Pico_Display_Pack_documentation#quickstart-script).  If you are powering it via a LiPo shim soldered in place, it must be switched ON for Thonny to detect the Pico.  Incidentally the LiPo shim offers a handy way of switching the Pico on and off while holding down BOOTSEL when trying to flash a Pico.  With the latest Pimoroni firmware you can use Thonny with the Pico and all Pimoroni hardware packs with MicroPython support.

<img src="https://cdn.shopify.com/s/files/1/0174/1800/products/pico-addons-3_1024x1024.jpg" width=450/>

## Pimoroni Wireless Pack
Pimoroni also have a Wireless networking pack for Pico available [here](https://shop.pimoroni.com/products/pico-wireless-pack) again addressable via MicroPython using the standard Pimoroni uf2 image.  The Wireless pack is built around an ESP32 microcontroller which has integrated Wi-Fi and dual-mode Bluetooth.  The following code will scan the local network for WiFI SSIDs:
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

<img src="https://cdn.shopify.com/s/files/1/0174/1800/products/pico-addons-13_1024x1024.jpg" width=450/>

## RFID reader
An RFID card reader is available from SB Component [here](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion).  Instructions for how to use:
* Install vanilla micropython image on your Pico
* git clone the repo [here](https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion)
* Connect via Thonny and copy three files from lib over to Pico
* Run `board_test.py`

![image](https://user-images.githubusercontent.com/12896870/144759767-a2800140-3704-457f-a927-0f6285b46ff8.png)

## C/C++
### Building the Pico Examples
Here are the steps you need to take to cross-compile, build and deploy the example code supplied with the Raspberry Pi Pico to the device:
* Update XCode CommandLineTools from Software Update in System Preferences or run the following command.  If it doesn't work you can update to the latest CommandLineTools for Xcode 13.1 [here](https://developer.apple.com/download/all/):
```
$ softwareupdate --all --install --force
```
* Install the Pico toolchain on your Mac using Homebrew per the instructions in section 9.1 [here](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf):
```
$ brew install cmake 
$ brew tap ArmMbed/homebrew-formulae 
$ brew install arm-none-eabi-gcc
```
* Pull down the [Pico SDK](https://github.com/raspberrypi/pico-sdk) and [Pico Example code](https://github.com/raspberrypi/pico-examples) as well as [Pico Extras](https://github.com/raspberrypi/pico-extras) per the instructions in section 2.1 [here](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
```
$ git clone -b master https://github.com/raspberrypi/pico-sdk.git 
$ cd pico-sdk 
$ git submodule update --init 
$ cd .. 
$ git clone -b master https://github.com/raspberrypi/pico-examples.git
$ git clone -b master https://github.com/raspberrypi/pico-extras.git
```
* Set up VSCode to work with the Pico toolchain.  This requires installing the CMake Tools and Cortex-Debug Extensions.
* Follow the instructions in section 7.1 [here](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf) on how to install VSCode.
* Open the pico-examples folder in VSCode.  In order to build you need to set the GCC target to `arm-none-eabi-gcc` and choose one of the targets in the pico-examples folder.  A good one to choose is `hello_usb`.  You can toggle between building "Debug" and "Release" executables by clicking on where it says "CMake: [Debug]: Ready" in the blue bottom bar. The default is to build a "Debug" enabled executable ready for SWD debugging.  Once everything is configured your VSCode setup will look like this:

<img width="1210" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/12896870/144769871-a1752267-ece7-48a5-9cf8-21a606eb1737.png">

* Copy the resulting build .uf2 file over to the Pico pressing BOOTSEL button and toggling LiPo shim on/off to mount USB Mass Storage device.  
Now run minicom to see the built file run.  If all is well you should see `printf` statements directed to USB output appear in `minicom`. To exit `minicom` press “ESC-X”:
```
$ minicom -b 115200 -o -D /dev/tty.usbmodem
```

### Building the Pimoroni Examples
The steps you need to take to cross-compile, build and deploy the example code supplied by Pimoroni for their various packs is similar but requires the explicit inclusion of `pico-extras` support:
* First you need to get the Pimoroni source code per the instructions [here](https://github.com/pimoroni/pimoroni-pico/blob/main/setting-up-the-pico-sdk.md):
```
$ git clone https://github.com/pimoroni/pimoroni-pico.git
$ cd pimoroni-pico
$ git submodule update --init
$ mkdir build
```
* Now we can try to build ALL the examples from the top level `pico-pimoroni` directory.
* We should be able to pull out the`wireless_time` example from the `build` directory for `pico_wireless` and run it.  Once running, pressing down the A button on the Pico wireless board to make the WiFi connection.  In order for it to work you have to edit the `secrets.h` in source and enter your WiFi creds in.  
* You'll note that `pico_audio` example didn't build. In order to build build it I first tried resorting to `cmake` at the command line and passing in the absolute dir for `PICO_POST_LIST_DIRS` after updating `pico-extras`.  This seemed to work but didn't actually build the binary:
```
$ cd ../pico-extras
$ git submodule update —init
$ cd ..
$ cmake .. -DPICO_SDK_DIR=/Desktop/CODE/PicoC/pico-sdk -DPICO_SDK_POST_LIST_DIRS=~/Desktop/CODE/PicoC/pico-extras
```
* There's an additional step needed.  You have to edit the top level Pimoroni `CMakeLists.txt` file per the instructions [here](https://github.com/raspberrypi/pico-extras/blob/master/README.md) to pull in the corresponding `.cmake`:
```
cmake_minimum_required(VERSION 3.12)

# Pull in PICO SDK (must be before project)
include(pico_sdk_import.cmake)
# This is the EXTRA line that's needed
include(pico_extras_import.cmake)

project(pico_examples C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
...
```
* Now you have to move over a copy of the corresponding `pico_extras_import.cmake` file to top level `pimoroni-pico` directory.  Finally you can now build the examples in VSCode.  It's possible to target just the `audio` target in `pimoroni-pico/examples/pico_audio` as shown below in VSCode.  The corresponding `demo.cpp` file located there has been modified to play Moonlight Sonata instead of the default track.  The small Python utility included [here](moonlightSonata.py) converts piano sheet music from notes into frequencies leveraging the setup already in place for the melody and rhythm tracks using them for the right and left hand piano parts respectively:

![image](https://user-images.githubusercontent.com/12896870/147891874-f1fcca7d-a321-4e4e-8b00-8ddc5bfeb78e.png)

* This results in a .uf2 build file where expected in the build subtree at `pimoroni-pico/build/examples/pico-audio/audio.uf2`.  Copy this file over to the Pico.  As soon as it boots you hear a recognisable if tinny version of Beethoven's tune.  You will need to have the Pimoroni Audio Pack connected to your Pico via a Pico Omnibus extension board as shown below and a 3.5 inch jack speaker connected to the Phones output socket with Hi Gain for maximum effect.  Click on the image to see it in action:

<img src="https://user-images.githubusercontent.com/12896870/144770679-5d29fac0-e289-42f8-9d39-afcb3cd2e070.png" width=500/>

### C/C++ Debugging
Serial Wire Debug (SWD) is a standard interface on Cortex-M-based microcontrollers which your host development machine can use to reset the board, load code into flash, and set the code running. Raspberry Pi Pico exposes the RP2040 SWD interface on three pins at the bottom edge of the board via a UART.  You'll have to connect them up to your host.  This requires that you connect the UART to your host which is easiest to do on a Raspberry Pi.  Debugging with SWD is covered in section 6 [here](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
You will also need to install `openocd` debug translator and set up .vscode/launch.json and .vscode/settings.json files to use it:
```
$ brew install openocd
```
