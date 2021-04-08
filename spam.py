import pyautogui
import time

times = int(input("How many times? "))
ready = int(input("how many second should i wait to execute the spam?: "))

time.sleep(ready)

for i in range(times):
    words = open('words.txt', 'r')
    for j in words:
        pyautogui.typewrite(j)
        pyautogui.press('enter')
        