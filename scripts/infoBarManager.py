import pyautogui
import time
import os

# Clicks on the x on the infobar 
# and sends f11 twice to refresh
def closeInfoBar():
    current_path = os.getcwd()
    print(f"Current working directory: {current_path}")
    location = pyautogui.locateCenterOnScreen('./images/image.png', confidence=0.8)
    
    if location:
        x, y = location
        pyautogui.click(x, y)
        pyautogui.press('f11')
        time.sleep(1)
        pyautogui.press('f11')
        print('Image 1 found')
        return True

    location = pyautogui.locateCenterOnScreen('./images/image2.png', confidence=0.8)
    
    if location:
        x, y = location
        pyautogui.click(x, y)
        pyautogui.press('f11')
        time.sleep(1)
        pyautogui.press('f11')
        print('Image 2 found')
        return True

def closeChromiumRestorePages():
    try:
        location = pyautogui.locateCenterOnScreen('./images/imagePages.png', confidence=0.8)
        
        if location:
            x, y = location
            pyautogui.click(x, y)
            time.sleep(1)
            pyautogui.click(x, y)
            print('Image Restore found')
    except Exception as e:
        pass