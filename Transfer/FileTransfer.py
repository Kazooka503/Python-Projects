from tkinter import *
from tkinter import filedialog
import glob
import os
import shutil
import datetime
import sys
import transfer

def browse_a():
    originPath = filedialog.askdirectory()
    e1.insert(0, originPath)

def browse_b():
    destinationPath = filedialog.askdirectory()
    e2.insert(0, destinationPath)

root = Tk()
root.title("Sample GUI")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=0, pady=0)

#Creating entry widgets
e1 = Entry(frame, width=40)
e2 = Entry(frame, width=40)

#Painting entry widgets to screen
e1.grid(row=1, column=1, columnspan=5, padx=20)
e2.grid(row=2, column=1, columnspan=5, padx=20)

#Creating button widgets
spacer = Label(frame, text = " ")
browse1 = Button(frame, text="Browse...", padx=20, command=browse_a)
browse2 = Button(frame, text="Browse...", padx=20, command=browse_b)
check = Button(frame, text="Check for files...", pady=10, command=transfer)
close = Button(frame, text="Close Program", padx=5, pady=10, command=exit)

#Painting widget onto the screen
spacer.grid(row=0, column=0, columnspan=4, pady=5)
browse1.grid(row=1, column=0, pady=5)
browse2.grid(row=2, column=0, pady=5)
check.grid(row=3, column=0)
close.grid(row=3, column=5, padx=5)

root.mainloop()


