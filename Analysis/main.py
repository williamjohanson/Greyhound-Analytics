# main.py
# Set up the code to iterate through as desired. Now utilising a GUI for inputs.
# Need to add user inputs for race meet and number of races and can then record the race data down.

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
import fill_txt_data

# GUI Specific Imports. 
import tkinter as tk
from tkinter import *
import os 
from PIL import Image, ImageTk

# Set canvas size variables.
HEIGHT = 900
WIDTH = 1500

# Globals.
MEETING = 0.1
TOTAL_RACES = 0.1

# Run the config function init to set up globals.
config.init() 

# Enter main functions for both GUI and analysis.
def fill_data(meet, race):
    """ Fill the text files with data. """
    global MEETING
    global TOTAL_RACES
    if race == None:
        try:
            MEETING = float(meet)
            results['text'] = str(int(MEETING))
        except ValueError:
            results['text'] = "Try entering meeting code again."
    elif meet == None:
        try:
            TOTAL_RACES = float(race)
            results['text'] = str(int(MEETING))
        except ValueError:
            results['text'] = "Try entering the number of races again."

    # Extract race information.
    if MEETING.is_integer() and TOTAL_RACES.is_integer():
        fill_txt_data.web_extract(int(MEETING), int(TOTAL_RACES))

def main(race_num):
    """ Main function to poll other functions. """
    try:
        new_race_file = race_file.get_race_file(race_num)

        runner_dict, num_runners = build_runners_dict(new_race_file)

        print_runners.runners_print(runner_dict)

        weighted_dict_1 = runner_weighting_dict.init(runner_dict, num_runners)

        weighted_dict_2 = grade_weight.grade_bias(new_race_file, weighted_dict_1)

        weighted_dict_3 = overall_stat(new_race_file, weighted_dict_2)

        weighted_dict_4 = box_stat(new_race_file, weighted_dict_3, runner_dict)

        weighted_dict_5 = recent_stat(new_race_file, weighted_dict_4, runner_dict)

        weighted_dict_6 = track_bias(weighted_dict_5, new_race_file)

        final_str_res = print_grades(runner_dict, weighted_dict_6) 

        results['text'] = final_str_res

    except:
        results['text'] = "There has been an error analysing this race."

#-------------------------------------------------------------------------------------------------#

# GUI Setup. 
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#263D42")

background_image = ImageTk.PhotoImage(Image.open('Images/bg.png'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

upper_frame = Frame(root,  bg='#42c2f4', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

frame = Frame(root,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

meet_textbox = Entry(upper_frame, font=40)
meet_textbox.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

race_textbox = Entry(upper_frame, font=40)
race_textbox.place(relx=0.5, rely=0,relwidth=0.5, relheight=0.5)

meet_exe_button = Button(upper_frame, text='Enter Meet No.', font=40, command=lambda: fill_data(meet_textbox.get(), None))
meet_exe_button.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)

race_exe_button = Button(upper_frame, text='Enter No. of Races', font=40, command=lambda: fill_data(None, race_textbox.get()))
race_exe_button.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.2, anchor='n')

textbox = Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

race_1_button = Button(frame, text='Analyse Race 1', font=40, command=lambda: main('race1.txt'))
race_1_button.place(relx=0, rely=0, relheight=0.33, relwidth=0.2)

race_2_button = Button(frame, text='Analyse Race 2', font=40, command=lambda: main('race2.txt'))
race_2_button.place(relx=0.2, rely=0, relheight=0.33, relwidth=0.2)

race_3_button = Button(frame, text='Analyse Race 3', font=40, command=lambda: main('race3.txt'))
race_3_button.place(relx=0.4, rely=0, relheight=0.33, relwidth=0.2)

race_4_button = Button(frame, text='Analyse Race 4', font=40, command=lambda: main('race4.txt'))
race_4_button.place(relx=0.6, rely=0, relheight=0.33, relwidth=0.2)

race_5_button = Button(frame, text='Analyse Race 5', font=40, command=lambda: main('race5.txt'))
race_5_button.place(relx=0.8, rely=0, relheight=0.33, relwidth=0.2)

race_6_button = Button(frame, text='Analyse Race 6', font=40, command=lambda: main('race6.txt'))
race_6_button.place(relx=0, rely=0.33, relheight=0.33, relwidth=0.2)

race_7_button = Button(frame, text='Analyse Race 7', font=40, command=lambda: main('race7.txt'))
race_7_button.place(relx=0.2, rely=0.33, relheight=0.33, relwidth=0.2)

race_8_button = Button(frame, text='Analyse Race 8', font=40, command=lambda: main('race8.txt'))
race_8_button.place(relx=0.4, rely=0.33, relheight=0.33, relwidth=0.2)

race_9_button = Button(frame, text='Analyse Race 9', font=40, command=lambda: main('race9.txt'))
race_9_button.place(relx=0.6, rely=0.33, relheight=0.33, relwidth=0.2)

race_10_button = Button(frame, text='Analyse Race 10', font=40, command=lambda: main('race10.txt'))
race_10_button.place(relx=0.8, rely=0.33, relheight=0.33, relwidth=0.2)

race_11_button = Button(frame, text='Analyse Race 11', font=40, command=lambda: main('race11.txt'))
race_11_button.place(relx=0, rely=0.67, relheight=0.33, relwidth=0.2)

race_12_button = Button(frame, text='Analyse Race 12', font=40, command=lambda: main('race12.txt'))
race_12_button.place(relx=0.2, rely=0.67, relheight=0.33, relwidth=0.2)

race_13_button = Button(frame, text='Analyse Race 13', font=40, command=lambda: main('race13.txt'))
race_13_button.place(relx=0.4, rely=0.67, relheight=0.33, relwidth=0.2)

race_14_button = Button(frame, text='Analyse Race 14', font=40, command=lambda: main('race14.txt'))
race_14_button.place(relx=0.6, rely=0.67, relheight=0.33, relwidth=0.2)

race_15_button = Button(frame, text='Analyse Race 15', font=40, command=lambda: main('race15.txt'))
race_15_button.place(relx=0.8, rely=0.67, relheight=0.33, relwidth=0.2)

bg_colour = 'white'
results = Label(lower_frame, anchor='n', justify='left', bd=4)
results.config(font=40, bg=bg_colour)
results.place(relwidth=1, relheight=1)

root.mainloop()
