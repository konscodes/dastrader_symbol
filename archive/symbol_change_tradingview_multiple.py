from pynput.keyboard import Key, Controller, GlobalHotKeys
import pyperclip
import time
import pygetwindow as gw

# Locating DAS window
#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]
tv1 = gw.getWindowsWithTitle('TV1')[0]
tv2 = gw.getWindowsWithTitle('TV2')[0]
tv3 = gw.getWindowsWithTitle('TV3')[0]
tv4 = gw.getWindowsWithTitle('TV4')[0]
print('\nWorking \nPress F12 to exit')

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

def main_function(dashotkey, tv_window):
    active_window = gw.getActiveWindow().title
    title_match_list = ['Intensity', 'Ultra', 'lounge', 'Monitor', 'Scan', 'Chat', 'CHAT']
    if any(title in active_window for title in title_match_list):
        start_time = time.time()
        time.sleep(0.1)
        copy()
        time.sleep(0.01)
        symbol = pyperclip.paste()
        print(symbol)
        das.activate()
        press_key(dashotkey)
        paste()
        press_key(Key.enter)
        time.sleep(0.3)
        tv_window.activate()
        time.sleep(0.1)
        for character in symbol:
            keyboard.type(character)
            time.sleep(0.05)
        press_key(Key.enter)
        print('--- %s seconds ---' % (time.time() - start_time))
    else:
        print('I3 not active!')

# Pass DAS script hotkey into main function
def transfer_function1():
    main_function(DASHOTKEY1, tv1)

def transfer_function2():
    main_function(DASHOTKEY2, tv2)
    
def transfer_function3():
    main_function(DASHOTKEY3, tv3)

def transfer_function4():
    main_function(DASHOTKEY4, tv4)

def exit_function():
    exit()

# Assign Python hotkeys to DAS script hotkeys
HOTKEY1 = '<F1>'
HOTKEY2 = '<F2>'
HOTKEY3 = '<F3>'
HOTKEY4 = '<F4>'
HOTKEY6 = '<F12>'

DASHOTKEY1 = Key.f1
DASHOTKEY2 = Key.f2
DASHOTKEY3 = Key.f3
DASHOTKEY4 = Key.f4

with GlobalHotKeys({
        HOTKEY1 : transfer_function1,
        HOTKEY2 : transfer_function2,
        HOTKEY3 : transfer_function3,
        HOTKEY4 : transfer_function4,
        HOTKEY6 : exit_function}) as MappedResult:
    MappedResult.join()

# TODO 
# Reduce copipaste in the code somehow