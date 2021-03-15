from pynput.mouse import Listener, Button, Controller
import pyautogui as pya
import time
import pygetwindow as gw
import keyboard
import pyperclip

#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]

mouse = Controller()

# Global variables for detecting double_click
CLICK_TIME = 0
RELEASE_TIME = 0
DIFFERENCE = 0

print('\nWorking \n')

def double_click(x, y, button, pressed):
    global RELEASE_TIME
    global CLICK_TIME
    global DIFFERENCE

    if pressed and button == Button.right:
        CLICK_TIME = time.time()
        DIFFERENCE = CLICK_TIME - RELEASE_TIME
        if DIFFERENCE < 0.25:
            main_function()
    else:
        RELEASE_TIME = time.time()
    
    return CLICK_TIME, RELEASE_TIME

def main_function():
    start_time = time.time()
    mouse.click(Button.left, 2)
    time.sleep(0.2)
    keyboard.send("ctrl+c")
    time.sleep(0.01)
    print(pyperclip.paste())
    das.activate()
    keyboard.send("F5")
    keyboard.send("ctrl+v+enter")
    print("--- %s seconds ---" % (time.time() - start_time))

with Listener(on_click=double_click) as mapped_result:
    mapped_result.join() 