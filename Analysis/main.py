# main.py
# Set up the code to iterate through as desired. 
# GUI code has currently been commented out and shall be replaced at some point.

# Imports. 
import race_file
import config 
from runners_dict import build_runners_dict 
import print_runners 
import runner_weighting_dict 
import grade_weight 
from overall_weight import overall_stat 
from box_weight import box_stat 
from recent_weight import recent_stat 
from track_weight import track_bias 
from print_func import print_grades 

"""GUI Specific Imports. 
import tkinter as tk
from tkinter import *
import os """

# Run the config function init to set up globals.
config.init() 

# Constantly running while loop.
#while(1):
def main():
    """ Main function to poll other functions. """

#global race_sel # Define as global within the function

    new_race_file = race_file.get_race_file()#)race_sel) # Get the new extended form race file to analyse the next race. Currently an input for each individual race.
    #---------------------------------------------------------------------------------------------#
    """Improvement: Iterate through all races at once with only input being how many races?"""
    #---------------------------------------------------------------------------------------------#

    runner_dict, num_runners = build_runners_dict(new_race_file)

    print_runners.runners_print(runner_dict)

    weighted_dict_1 = runner_weighting_dict.init(runner_dict, num_runners)

    weighted_dict_2 = grade_weight.grade_bias(new_race_file, weighted_dict_1)

    weighted_dict_3 = overall_stat(new_race_file, weighted_dict_2)

    weighted_dict_4 = box_stat(new_race_file, weighted_dict_3, runner_dict)

    weighted_dict_5 = recent_stat(new_race_file, weighted_dict_4, runner_dict)

    weighted_dict_6 = track_bias(weighted_dict_5, new_race_file)

    #my_gui = MyFirstGUI(gui, runner_dict, weighted_dict_6)

    print_grades(runner_dict, weighted_dict_6) 

#-------------------------------------------------------------------------------------------------#
""" GUI Setup. 
root = tk.Tk()

canvas = tk.Canvas(root, height=900, width=900, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

exeButton = tk.Button(root, text="Execute", padx=10, pady=5, fg="white", bg="#263D42", command=main)
exeButton.pack()

tkvar = StringVar(root) # Create a tkinter variable
tkvar.set("Select a race!")
race_numbers = {'race1.txt', 'race2.txt', 'race3.txt', 'race4.txt', 'race5.txt', 'race6.txt', 'race7.txt', 'race8.txt', 'race9.txt', 'race10.txt', 'race11.txt', 'race12.txt', 'race13.txt', 'race14.txt', 'race15.txt'}
raceDropdown = OptionMenu(root, tkvar, *race_numbers)
raceDropdown.pack()

global race_sel
race_sel = tkvar.get()

root.mainloop()"""
