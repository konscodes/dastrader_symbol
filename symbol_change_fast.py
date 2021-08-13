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
click_time = 0
release_time = 0
difference = 0
print("\nWorking \n")

# Double click function
def double_click(x, y, button, pressed):
    global release_time
    global click_time
    global difference

    if pressed and button == Button.left:
        click_time = time.time()
        difference = click_time - release_time
        if difference < 0.25:
            #print("Double click!")
            main_function()
    else:
        release_time = time.time()
    
    return click_time, release_time

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