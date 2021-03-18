from pynput.mouse import Listener, Button, Controller
import time
import pygetwindow as gw
import keyboard
import pyperclip

# Locating DAS window
#print(gw.getAllTitles())
#print(gw.getWindowsWithTitle("DASTrader"))
das = gw.getWindowsWithTitle("DASTrader")[0]
mouse = Controller()

# Global variables for detecting double_click
CLICK_TIME = 0
RELEASE_TIME = 0
DIFFERENCE = 0
print("\nWorking \n")

# Double click function
def double_click(x, y, button, pressed):
    global RELEASE_TIME
    global CLICK_TIME
    global DIFFERENCE

    if pressed and button == Button.left:
        CLICK_TIME = time.time()
        DIFFERENCE = CLICK_TIME - RELEASE_TIME
        if DIFFERENCE < 0.25:
            #print("Double click!")
            main_function()
    else:
        RELEASE_TIME = time.time()
    
    return CLICK_TIME, RELEASE_TIME


# Main function
def main_function():
    active_window = gw.getActiveWindow().title
    title_match_list = ["Intensity", "Ultra", "lounge", "Monitor", "Scan", "Chat", "CHAT"]
    if any(title in active_window for title in title_match_list):
        start_time = time.time()
        time.sleep(0.3)
        keyboard.send("ctrl+c")
        time.sleep(0.01)
        print(pyperclip.paste())
        das.activate()
        keyboard.send("F5")
        keyboard.send("ctrl+v+enter")
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("I3 not active!")

# Listener
with Listener(on_click=double_click) as mapped_result:
    mapped_result.join() 