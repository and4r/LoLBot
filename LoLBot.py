import pyautogui
import keyboard
import win32gui
import time
print("Activate autododge (X), or auto-accept (Y), or exit the program (ENTER)? ")
def asker():
   while True:
    if keyboard.read_key() == "x":
        auto_dodge()
    elif keyboard.read_key() == "y":
        auto_accept()
    elif keyboard.read_key() == "enter":
        exit()
    else:
        asker()
def auto_accept():
    print("Autoaccept activated! Keep your client open.")
    while True:
        if pyautogui.locateOnScreen("accept.png", confidence=0.5):
            point = pyautogui.locateOnScreen("accept.png", confidence=0.5)
            x, y = pyautogui.center(point)
            pyautogui.click(x,y)
            exit()
def auto_dodge():

    windowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if windowName == "League of Legends":
        win32gui.MoveWindow(win32gui.GetForegroundWindow(), 700, 300, 1280, 720, 100)
        pyautogui.moveTo(1350, 880)
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')
        pyautogui.keyDown('alt')
        pyautogui.press('f4')
        pyautogui.keyUp('alt')
        exit()
    elif windowName != "League of Legends":
            print("To use this feature you must have League Of Legends running and it must be maximised.")
            time.sleep(2)
            exit()
asker()