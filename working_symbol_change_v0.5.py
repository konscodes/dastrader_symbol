from pywinauto import Application
from pywinauto import keyboard as pywinauto_keyboard
from pynput.mouse import Listener, Button, Controller
import pyperclip
import time

mouse = Controller()

app = Application(backend="win32").connect(class_name="AfxMDIFrame100").window(class_name="AfxMDIFrame100")

#app.Montage327701.print_control_identifiers()
#app.Last32770.print_control_identifiers()

montage_level1 = app.Last32770
symbol = montage_level1.Edit

# Global variables for detecting double_click
CLICK_TIME = 0
RELEASE_TIME = 0
DIFFERENCE = 0

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
    pywinauto_keyboard.send_keys('^c')
    copy_text = pyperclip.paste()
    symbol.set_edit_text(copy_text)
    symbol.send_keystrokes("{ENTER}")
    print("--- %s seconds ---" % (time.time() - start_time))

with Listener(on_click=double_click) as mapped_result:
    mapped_result.join() 