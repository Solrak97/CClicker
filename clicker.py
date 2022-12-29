import pyautogui
from dotenv import load_dotenv
import os
import time

# Carga de ambiente
load_dotenv()
W_TIME = float(os.environ['W_TIME'])
N_CLICKS = int(os.environ['N_CLICKS'])
D_TIME = float(os.environ['D_TIME'])


time.sleep(D_TIME)
if N_CLICKS > 0:
    for i in range(N_CLICKS):
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(W_TIME)
else:
    while True:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(W_TIME)