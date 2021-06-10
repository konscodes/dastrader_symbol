from pynput.keyboard import Key, Controller, GlobalHotKeys
import pyperclip
import time
import pygetwindow as gw

# Locating DAS window
#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]
print('\nWorking \n')

keyboard = Controller()

def copy():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def paste():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def press_key(dashotkey):
    keyboard.press(dashotkey)
    keyboard.release(dashotkey)

def main_function(dashotkey):
    active_window = gw.getActiveWindow().title
    title_match_list = ["Intensity", "Ultra", "lounge", "Monitor", "Scan", "Chat", "CHAT", "%"]
    if any(title in active_window for title in title_match_list):
        start_time = time.time()
        time.sleep(0.1)
        copy()
        time.sleep(0.01)
        print(pyperclip.paste())
        das.activate()
        press_key(dashotkey)
        paste()
        press_key(Key.enter)
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("I3 not active!")

# Pass DAS script hotkey into main function
def transfer_function1():
    main_function(DASHOTKEY1)

def transfer_function2():
    main_function(DASHOTKEY2)
    
def transfer_function3():
    main_function(DASHOTKEY3)

def transfer_function4():
    main_function(DASHOTKEY4)

def transfer_function5():
    main_function(DASHOTKEY5)

# Assign Python hotkeys to DAS script hotkeys
HOTKEY1 = "<F1>"
HOTKEY2 = "<F2>"
HOTKEY3 = "<F3>"
HOTKEY4 = "<F4>"
HOTKEY5 = "<F5>"

DASHOTKEY1 = Key.f1
DASHOTKEY2 = Key.f2
DASHOTKEY3 = Key.f3
DASHOTKEY4 = Key.f4
DASHOTKEY5 = Key.f5

with GlobalHotKeys({
        HOTKEY1 : transfer_function1,
        HOTKEY2 : transfer_function2,
        HOTKEY3 : transfer_function3,
        HOTKEY4 : transfer_function4,
        HOTKEY5 : transfer_function5}) as MappedResult:
    MappedResult.join()

# TODO 
# Reduce copipaste in the code somehow