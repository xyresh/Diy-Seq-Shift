#
#   File: code.py
#
#   Author: mrayo(xyresh)
#



import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#declaration of Keys to send via USB to PC 
#feel free to change the keys to your liking
key_A=Keycode.V
key_SPACE = Keycode.C
keyboard=Keyboard(usb_hid.devices)


led = digitalio.DigitalInOut(board.LED)

led.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP21)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

button2 = digitalio.DigitalInOut(board.GP22)
button2.switch_to_input(pull=digitalio.Pull.DOWN)






while True:
    if button1.value:
        led.value = True
        keyboard.press(key_A)
        time.sleep(0.01)
        led.value = False
    if button2.value:
        led.value = True
        keyboard.press(key_SPACE)
        time.sleep(0.01)
        led.value = False

    if button1.value == False:
        keyboard.release(key_A)

    if button1.value == False:
        keyboard.release(key_SPACE)

