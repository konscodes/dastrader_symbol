from pywinauto import Application
from pywinauto import keyboard as PywinautoKeyboard
from pynput.mouse import Listener, Button, Controller
import pyperclip
import time

Mouse = Controller()

app = Application(backend="win32").connect(class_name="AfxMDIFrame100").window(class_name="AfxMDIFrame100")

#app.Montage327701.print_control_identifiers()
#app.Last32770.print_control_identifiers()

MontageLevel1 = app.Last32770
Symbol = MontageLevel1.Edit

# Global variables for detecting DoubleClick
Clicktime = 0
Releasetime = 0
Difference = 0

def DoubleClick(x, y, button, pressed):
    global Releasetime
    global Clicktime
    global Difference

    if pressed and button == Button.right:
        Clicktime = time.time()
        Difference = Clicktime - Releasetime
        if Difference < 0.25:
            MainFunction()
    else:
        Releasetime = time.time()
    
    return Clicktime, Releasetime

def MainFunction():
    start_time = time.time()
    Mouse.click(Button.left, 2)
    PywinautoKeyboard.send_keys('^c')
    CopyText = pyperclip.paste()
    Symbol.set_edit_text(CopyText)
    Symbol.send_keystrokes("{ENTER}")
    print("--- %s seconds ---" % (time.time() - start_time))

with Listener(on_click=DoubleClick) as MappedResult:
    MappedResult.join() 