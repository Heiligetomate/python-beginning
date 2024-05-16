import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="r")
TOGGLE_KEY_POS = KeyCode(char="s")
clicking = False
ban = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.press(Button.left)
            mouse.release(Button.left)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


def toggle_mouse_ban(key):
    if key == TOGGLE_KEY_POS:
        global ban
        ban = not ban


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

