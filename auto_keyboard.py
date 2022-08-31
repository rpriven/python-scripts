#!/usr/bin/python3

# Auto Keyboard (for games)
# This script turns on and off using the 't' key (or you can change it below)
# When activated, it presses and releases the specified key(s) until deactivated

import time
import threading
# in shell: pip install pynput
from pynput import keyboard

# from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key, Controller

try:
    # Activates / Deactivates the clicking
    TOGGLE_KEY = KeyCode(char="t")

    clicking = False
    keyboard = Controller()

    def quick_enter():
        while True:
            if clicking:
                # Modify this code here to press different keys
                keyboard.press('g')
                # Increase the delay if you run into errors
                time.sleep(0.00001)
                keyboard.release('g')

                '''
                keyboard.press('5')
                time.sleep(0.00001)
                keyboard.release('5')
                keyboard.press(Key.enter)
                time.sleep(0.075)
                keyboard.release(Key.enter)
                '''

                '''
                keyboard.press(Key.enter)
                keyboard.press('4')
                time.sleep(0.01)
                keyboard.release('4')
                keyboard.press('3')
                time.sleep(0.01)
                keyboard.release('3')
                keyboard.press('2')
                time.sleep(0.01)
                keyboard.release('2')
                keyboard.press('1')
                time.sleep(0.01)
                keyboard.release('1')
                '''
                            
            # creates a pause so that it detects separate clicks 
            # (also in order to toggle)
            time.sleep(0.0001)

    def toggle_event(key):
        if key == TOGGLE_KEY:
            global clicking
            clicking = not clicking

    click_thread = threading.Thread(target=quick_enter)
    click_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

except KeyboardInterrupt:
    print('KeyboardInterrupt')
