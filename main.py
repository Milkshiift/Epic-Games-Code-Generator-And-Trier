import time
import random
import pyautogui
import keyboard

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
time.sleep(5)

while True:
    key = ""
    for x in range(0, 20):
        key_char = random.choice(chars)
        key = key + key_char
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
    keyboard.write(str(key))
    time.sleep(0.1)
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
