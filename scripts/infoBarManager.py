import pyautogui
import time

# Clicks on the x on the infobar 
# and sends f11 twice to refresh
def closeInfoBar():
    location = pyautogui.locateCenterOnScreen('./image.png', confidence=0.8)
    
    if location:
        x, y = location
        pyautogui.click(x, y)
        pyautogui.press('f11')
        time.sleep(1)
        pyautogui.press('f11')
