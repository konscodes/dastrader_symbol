# pywinauto_dastrader_symbol
Double click on ISW scanner alers to change DAS montage symbol.
Lazy way to switch DAS montage symbol by selecting ISW scanner alert. 
It would be nice to have a native integration between ISW and DAS like in Tradeideas but until then this script will win you a second or two. 

Idea: <br>
Change DAS symbol by clicking on ISW scanner alert.

Problem:<br>
This kind of integration is not natively supported. Need to manually type/copy-paste alerts from the scanner into DAS.

Solution:<br>
Simple python script that sends scanner ticker into clipboard and uses pywinauto to update montage.

Notes:
- script will overwrite existing clipboard
- can be set to go with mouse button click or keyboard hotkey
- mose script is set for right mouse double click by default
- keyboard script is set to F8 by default

Requirements:<br>
Pythin 3.8.0<br>
Pywinauto 0.6.8<br>
Pynput 1.6.7<br>
keyboard, pyperclip, time libraries<br>

Preparation:
- Download working_symbol_change_mouse script and install all the requirements above
- Run the script (open cmd in the directory with script; enter: py script_name.py)

How to use:
1. Make sure that DAS is running
2. Double click right mouse button on the alerted ticker
3. Profit ;) the correct symbol should be set in montage


Change log:<br>
v0.4
Added mouse double click script

v0.3
Added hotkey module to run the script

v0.2
Basic functionality reached
