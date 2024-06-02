import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="1")
clicking = False
ban = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.press(Button.left)
            mouse.release(Button.left)
        time.sleep(0.01)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

