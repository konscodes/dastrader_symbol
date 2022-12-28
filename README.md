# DasTrader Symbol 
Double click on ISW scanner alers to change DAS montage symbol.
Lazy way to switch DAS montage symbol by selecting ISW scanner alert. 
It would be nice to have a native integration between ISW and DAS like in Tradeideas but until then this script will win you a second or two. 

## What
Script to change DAS montage symbol when clicking on ISW scanner alert.
Simple python script that sends scanner ticker into clipboard and pastes into active DAS montage.

## Why
This kind of integration is not natively supported. Need to manually type/copy-paste alerts from the scanner into DAS.

## How to use
1. Set the DAS hotkeys to activate the correct montage
![image](https://user-images.githubusercontent.com/6221944/209818665-bf9aa826-8ef3-4f64-8175-a2f436b9e5cf.png)
![image](https://user-images.githubusercontent.com/6221944/209818804-2ea13a8e-0590-4483-8e1c-e87a3fb608e0.png)

2. Make sure that DAS is running
3. Download symbol_change_keyboard script and install all the requirements above
4. Run the script (open cmd in the directory with script; enter: python script_name.py)
5. Double click on scanner alert to select it and press the hotkey
6. Correct symbol should be set in montage automatically

### Notes
- script will overwrite existing clipboard
- keyboard script is set to quit on F12 by default

### Requirements
- python 3.8.0+
- pygetwindow 0.0.9
- keyboard, time libraries

### Change log
- Removed unnecessary scripts and libraries
- Added mouse double click script
- Added hotkey module to run the script
- Basic functionality reached
