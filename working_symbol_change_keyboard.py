from pywinauto import Application
from pywinauto import keyboard as PywinautoKeyboard
from pynput.mouse import Button, Controller
import keyboard
import pyperclip
import time

Mouse = Controller()

app = Application(backend="win32").connect(class_name="AfxMDIFrame100").window(class_name="AfxMDIFrame100")

#app.Montage327701.print_control_identifiers()
#app.Last32770.print_control_identifiers()

MontageLevel1 = app.Last32770
Symbol = MontageLevel1.Edit

def MainFunction():
    Mouse.click(Button.left, 2)
    PywinautoKeyboard.send_keys('^c')
    CopyText = pyperclip.paste()
    Symbol.set_edit_text(CopyText)
    Symbol.send_keystrokes("{ENTER}")

keyboard.add_hotkey('F8', MainFunction)
keyboard.wait()