import pyautogui
import time

for i in range(100):
    pyautogui.typewrite("spam message...")
    time.sleep(1)
    pyautogui.press("enter")
