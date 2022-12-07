# import the required modules
import keyboard
import time
import pygetwindow as gw

# locating DAS window
#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle('DASTrader'))
das = gw.getWindowsWithTitle('DASTrader')[0]
print('\nWorking \nPress F12 to exit')

# define main function receives arguments form transfer func
def main(daskey):
    active_window = gw.getActiveWindow().title
    title_match_list = ["Intensity", "Ultra", "lounge", "Monitor", "Scan", "Chat", "CHAT", "%", "Watchlist"]
    if any(title in active_window for title in title_match_list):
        start_time = time.time()
        keyboard.press_and_release('ctrl + c')
        time.sleep(0.01)
        das.activate()
        keyboard.press_and_release(daskey)
        keyboard.press_and_release('ctrl + v')
        keyboard.press_and_release('enter')
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("I3 not active!")

# wait for the keys to be pressed
keyboard.add_hotkey('F1', lambda: main('F1'))
keyboard.add_hotkey('F2', lambda: main('F2'))
keyboard.add_hotkey('F3', lambda: main('F3'))
keyboard.add_hotkey('F4', lambda: main('F4'))
keyboard.add_hotkey('F5', lambda: main('F5'))
keyboard.add_hotkey('F6', lambda: main('F6'))
keyboard.add_hotkey('F7', lambda: main('F7'))
keyboard.add_hotkey('F8', lambda: main('F8'))
keyboard.add_hotkey('F9', lambda: main('F9'))

# run the program until 'F12' is pressed
keyboard.wait('F12')