# GUI Specific Imports. 
import tkinter as tk
from tkinter import *
import os 
from PIL import Image, ImageTk

# Set canvas size variables.
HEIGHT = 900
WIDTH = 1500

# GUI Setup. 
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#263D42")

background_image = ImageTk.PhotoImage(Image.open('bg.png'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

frame = Frame(root,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

textbox = Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = Button(frame, text='Get Race Info', font=40, command=lambda: get_weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)

"""

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
race_sel = tkvar.get()"""

root.mainloop()