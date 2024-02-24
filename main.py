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
    print("Running...")
    while True:
        try:
            link_attack = pyautogui.locateOnScreen(
                "./images/link_attack.png", confidence=0.8
            )
            if link_attack:
                pydirectinput.press("r")
                time.sleep(0.2)
        except ImageNotFoundException:
            time.sleep(0.1)

        try:
            revive = pyautogui.locateOnScreen("./images/revive.png", confidence=0.9)
            if revive:
                pydirectinput.keyDown("v")
                time.sleep(2)
                pydirectinput.keyUp("v")
                time.sleep(0.5)
        except ImageNotFoundException:
            time.sleep(0.1)

        try:
            repeat_prompt = pyautogui.locateOnScreen(
                "./images/repeat.png", confidence=0.8
            )
            if repeat_prompt:
                pydirectinput.press("3")
                time.sleep(0.3)
                pydirectinput.press("enter")
        except ImageNotFoundException:
            repeat_prompt = None
            time.sleep(0.2)

        try:
            next_button = pyautogui.locateOnScreen("./images/next.png", confidence=0.8)
            if next_button and repeat_prompt is None:
                autoit.mouse_click("left")
                time.sleep(0.2)
        except ImageNotFoundException:
            time.sleep(0.2)

        try:
            confirm = pyautogui.locateOnScreen("./images/confirm.png", confidence=0.9)
            if confirm:
                autoit.mouse_click("left")
                time.sleep(0.5)
        except ImageNotFoundException:
            time.sleep(0.2)


# def trade_goods():
#     autoit.mouse_click("right")
#     time.sleep(2)
#     pydirectinput.press("up")
#     time.sleep(1)
#     autoit.mouse_click("left")
#     time.sleep(1)

#     while True:
#         try:
#             trade_treasure = pyautogui.locateOnScreen(
#                 "./images/trade.png", confidence=0.95
#             )
#             if trade_treasure:
#                 autoit.mouse_click("left")
#                 time.sleep(1)
#                 pydirectinput.press("left", presses=20, interval=0.05)
#                 time.sleep(1)
#                 autoit.mouse_click("left")
#                 time.sleep(2)
#                 pydirectinput.press("down")
#                 time.sleep(1)
#                 autoit.mouse_click("left")
#                 time.sleep(1)
#                 pydirectinput.press("3")
#                 time.sleep(1)
#                 pydirectinput.press("up")
#                 time.sleep(1)
#                 autoit.mouse_click("left")
#                 time.sleep(1)
#                 autoit.mouse_click("left")
#                 time.sleep(1)
#                 autoit.mouse_click("right")
#                 time.sleep(1)
#                 autoit.mouse_click("right")
#                 time.sleep(1)
#                 pydirectinput.press("down")
#                 time.sleep(1)
#                 autoit.mouse_click("left")
#                 break
#         except ImageNotFoundException:
#             autoit.send("{up}")
#             time.sleep(1)


def transmute():
    time.sleep(3)
    while True:
        # try:
        #     transmute = pyautogui.locateOnScreen(
        #         "./images/transmute.png", confidence=0.95
        #     )
        #     if transmute:
        #         autoit.mouse_click("left")
        #         time.sleep(0.2)
        try:
            voucher = pyautogui.locateOnScreen(
                "./images/voucher_check.png", confidence=0.9
            )
            if voucher:
                autoit.mouse_click("left")
                time.sleep(0.2)
                # trade_goods()
                exit()
        except ImageNotFoundException:
            autoit.mouse_click("left")
            time.sleep(0.3)
        # except ImageNotFoundException:
        #     autoit.send("{down}")
        #     time.sleep(1)


repeat_quest()
# transmute()
