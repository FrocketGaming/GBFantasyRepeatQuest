import pyautogui
from pyautogui import ImageNotFoundException
import pydirectinput
import autoit
import time


def repeat_quest():
    while True:
        try:
            repeat_prompt = pyautogui.locateOnScreen(
                "./images/repeat.png", confidence=0.9
            )
            if repeat_prompt:
                print("repeating quest")
                pydirectinput.press("3")
                time.sleep(0.5)
                pydirectinput.press("enter")
        except ImageNotFoundException:
            repeat_prompt = None
            time.sleep(0.5)

        try:
            next_button = pyautogui.locateOnScreen("./images/next.png", confidence=0.8)
            if next_button and repeat_prompt is None:
                autoit.mouse_click("left")
                time.sleep(1)
        except ImageNotFoundException:
            next_button = None
            time.sleep(0.5)

        try:
            confirm = pyautogui.locateOnScreen("./images/confirm.png", confidence=0.9)
            if confirm:
                autoit.mouse_click("left")
                time.sleep(0.5)
        except ImageNotFoundException:
            confirm = None


repeat_quest()
