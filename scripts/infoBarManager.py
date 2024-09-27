import pyautogui
import time

# Clicks on the x on the infobar 
# and sends f11 twice to refresh
def closeInfoBar():
    x, y = pyautogui.locateCenterOnScreen('./image.png')
    pyautogui.click(x,y)

    pyautogui.press('f11')
    time.sleep(1)
    pyautogui.press('f11')
