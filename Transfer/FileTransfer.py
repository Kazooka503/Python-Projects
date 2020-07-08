from tkinter import *
from tkinter import filedialog
from pathlib import Path
import glob
import os
import shutil
import datetime
import sys

def FileListCapture(path, type):
    #returns a list of filenames that match path
    return glob.glob(path + "*" + type)

def browse_a():
    x = os.path.splitdrive(filedialog.askdirectory())
    y = x[1]
    e1.insert(0, y)

def browse_b():
    x = os.path.splitdrive(filedialog.askdirectory())
    y = x[1]
    e2.insert(0, y)

def check():
    originPath = e1.get() + "/"
    destinationPath = e2.get() + "/"
    fileType = ".txt"
    source = FileListCapture(originPath, fileType)
    print(originPath)
    print(destinationPath)
    print(source)
    for file in source:
        #Get last modified date and current date
        modDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        currentDate = datetime.datetime.today()

        filePathList = file.split("\\") # create list from filepath
        filename = filePathList[-1]

        modifyDateLimit = modDate + datetime.timedelta(days=1)
        if modifyDateLimit > currentDate:
            shutil.copy2(file, destinationPath + filename)
    
root = Tk()
root.title("File Transfer")

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
check = Button(frame, text="Check for files...", pady=10, command=check)
close = Button(frame, text="Close", padx=20, pady=10, command=exit)

#Painting widget onto the screen
spacer.grid(row=0, column=0, columnspan=4, pady=5)
browse1.grid(row=1, column=0, pady=5)
browse2.grid(row=2, column=0, pady=5)
check.grid(row=3, column=0)
close.grid(row=3, column=5, padx=5)




