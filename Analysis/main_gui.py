# GUI Specific Imports. 
import tkinter as tk
from tkinter import *
import os 
import main

# GUI Setup. 
root = tk.Tk()

canvas = tk.Canvas(root, height=900, width=900, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

exeButton = tk.Button(root, text="Execute", padx=10, pady=5, fg="white", bg="#263D42", command=main.main())
exeButton.pack()

tkvar = StringVar(root) # Create a tkinter variable
tkvar.set("Select a race!")
race_numbers = {'race1.txt', 'race2.txt', 'race3.txt', 'race4.txt', 'race5.txt', 'race6.txt', 'race7.txt', 'race8.txt', 'race9.txt', 'race10.txt', 'race11.txt', 'race12.txt', 'race13.txt', 'race14.txt', 'race15.txt'}
raceDropdown = OptionMenu(root, tkvar, *race_numbers)
raceDropdown.pack()

global race_sel
race_sel = tkvar.get()

root.mainloop()