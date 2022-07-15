import time
import random
import pyautogui
import keyboard

time.sleep(5)

while True:
    time.sleep(2)
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    if r != 7 and g != 77 and b != 144:  # 7, 77, 144
        break
    pyautogui.moveTo(x, y-60)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+a, backspace')
    code = random.randint(10000000000000000000, 99999999999999999999)
    keyboard.write(str(code))
    time.sleep(0.1)
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
