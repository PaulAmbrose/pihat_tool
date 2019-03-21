from graphics_pa_gui import *
import sys
import pi_hat_tool_dice

try:
    opening_menu = window_pa.create_window_pa("opening_menu", "pauls pi hat",
                                              "black", 300, 300)
except:
    print("fail_line5_python_gui.py_invalid name or data type")
    sys.exit()

try:
    five_button = button_pa.button_array_pa(opening_menu,
                                            ["Roll Dice",
                                             "Graphics display",
                                             "Thermometer",
                                             "Detect Movement",
                                             "Hygrometer"
                                             ], 100, 100, 900, 255, "blue",
                                            "green")
except:
    print("fail_linenumber_file")
    sys.exit()

mouseclick = opening_menu.getMouse()

try:
    five_button_select = button_pa.button_array_opt_pa(five_button, mouseclick)
except:
    print("fail_linenumber_file")
    sys.exit()

if five_button_select == 0:
    pi_hat_tool_dice.roll_dice
    
if five_button_select == 1:
    print("display")
if five_button_select == 2:
    print("therm")
if five_button_select == 3:
    print("movement")
if five_button_select == 4:
    print("hygrom")