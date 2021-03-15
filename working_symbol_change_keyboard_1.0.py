from pynput.mouse import Button, Controller
import keyboard
import pyperclip
import time
import pygetwindow as gw

print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]

print('\nWorking \n')

#Reduce copipaste somehow
#Hotkey to only be active with ISW windows

def hotkey1():
    main_function("F1")

def hotkey2():
    main_function("F2")
    
def hotkey3():
    main_function("F3")

def hotkey4():
    main_function("F4")

def hotkey5():
    main_function("F5")

def main_function(hotkey):
    active_window = gw.getActiveWindow().title
    if "DASTrader" in active_window:
        print("DAS!")
    else:
        start_time = time.time()
        time.sleep(0.2)
        keyboard.send("ctrl+c")
        time.sleep(0.01)
        print(pyperclip.paste())
        das.activate()
        keyboard.send(hotkey)
        keyboard.send("ctrl+v+enter")
        print("--- %s seconds ---" % (time.time() - start_time))
   
keyboard.add_hotkey('F1', hotkey1)
keyboard.add_hotkey('F2', hotkey2)
keyboard.add_hotkey('F3', hotkey3)
keyboard.add_hotkey('F4', hotkey4)
keyboard.add_hotkey('F5', hotkey5)
keyboard.wait()