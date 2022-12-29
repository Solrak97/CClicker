import pyautogui
from dotenv import load_dotenv
import os
import time
import keyboard

# Carga de ambiente
load_dotenv()
W_TIME = float(os.environ['W_TIME'])
N_CLICKS = int(os.environ['N_CLICKS'])
D_TIME = float(os.environ['D_TIME'])


time.sleep(D_TIME)
if N_CLICKS > 0:
    for i in range(N_CLICKS):
        time.sleep(W_TIME)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        if keyboard.is_pressed("ctrl+c"):
            break

else:
    while True:
        time.sleep(W_TIME)
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        if keyboard.is_pressed("ctrl+c"):
            break