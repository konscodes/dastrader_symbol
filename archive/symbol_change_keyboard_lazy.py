from pynput.mouse import Button, Controller
import keyboard
import pyperclip
import time
import pygetwindow as gw

# Locating DAS window
#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]
print('\nWorking \n')

# Main function
def main_function(scriptkey):
    active_window = gw.getActiveWindow().title
    title_match_list = ["Intensity", "Ultra", "Monitor", "Scan"]
    if any(title in active_window for title in title_match_list):
        start_time = time.time()
        time.sleep(0.1)
        keyboard.send("ctrl+c")
        time.sleep(0.01)
        print(pyperclip.paste())
        das.activate()
        keyboard.send(scriptkey)
        keyboard.send("ctrl+v+enter")
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("I3 not active!")

# Pass DAS script hotkey into main function
def scriptkey1():
    main_function("F1")

def scriptkey2():
    main_function("F2")
    
def scriptkey3():
    main_function("F3")

def scriptkey4():
    main_function("F4")

def scriptkey5():
    main_function("F5")

# Assign Python hotkeys to DAS script hotkeys
keyboard.add_hotkey('a', scriptkey1)
keyboard.add_hotkey('s', scriptkey2)
keyboard.add_hotkey('d', scriptkey3)
keyboard.add_hotkey('z', scriptkey4)
keyboard.add_hotkey('x', scriptkey5)
keyboard.wait()

# TODO 
# Reduce copipaste in the code somehow