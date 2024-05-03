from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Listener, KeyCode
import time as t

mouse = Controller()
keyboard = Controller()
KEY = KeyCode(char="a")


def click_at_position(position: tuple, time_sleep=0.7) -> None:
    mouse.position = position
    mouse.press(Button.left)
    mouse.release(Button.left)
    t.sleep(time_sleep)


def find_mouse_position(key):
    if key == KEY:
        print(mouse.position)


click_at_position((1131, 1419))
click_at_position((1184, 732))
keyboard.press(Key.space)
click_at_position((1459, 677))
click_at_position((1387, 473))
click_at_position((1289, 755))
click_at_position((936, 520))
click_at_position((1981, 1320))
click_at_position((1981, 1320))

with Listener(on_press=find_mouse_position) as listener:
    listener.join()
