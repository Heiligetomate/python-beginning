import keyboard
import keyboard as k
import time
from pynput.mouse import Controller, Button
import sys


def open_firefox_music():
    k.press_and_release('Windows, f, i, r')
    time.sleep(0.05)
    k.press_and_release('Enter')
    time.sleep(0.5)
    k.write("music.youtube.com")
    k.press_and_release('Enter')
    time.sleep(1.5)
    for i in range(3):
        k.press_and_release('Tab')


k.add_hotkey('r', open_firefox_music)
time.sleep(2000)
