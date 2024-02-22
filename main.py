import pyautogui
from pyautogui import ImageNotFoundException
import pydirectinput
import autoit
import time


def repeat_quest():
    """
    Looks for the repeat quest image and repeats the quest after every 10 rounds. It also looks for the next and confirm buttons to push through prompts. 
    This code uses pyautogui, autoit, and pydirectinput to automate the game.

    Pyautogui uses the images to find the buttons on the screen but inputs seem to be blocked by the game, so I used pydirectinput to send the key presses. 
    However, the mouse inputs from pydirectinput did not work so I finally implemented autoit to fix that issue.
    """
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
            time.sleep(0.2)

        try:
            next_button = pyautogui.locateOnScreen("./images/next.png", confidence=0.8)
            if next_button and repeat_prompt is None:
                autoit.mouse_click("left")
                time.sleep(1)
        except ImageNotFoundException:
            time.sleep(0.2)

        try:
            confirm = pyautogui.locateOnScreen("./images/confirm.png", confidence=0.9)
            if confirm:
                autoit.mouse_click("left")
                time.sleep(0.5)
        except ImageNotFoundException:
            time.sleep(0.2)


repeat_quest()
