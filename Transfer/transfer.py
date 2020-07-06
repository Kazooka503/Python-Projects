import glob
import os
import shutil 
import datetime

def FileListCapture(path, type):
    # returns a list of filename that matches file type/path
    return glob.glob(path + "*" + type)

originPath = "/Users/austi/Desktop/Folder_A/"
destinationPath = "/Users/austi/Desktop/Folder_B/"
fileType = ".txt"

# makes list of text filenames in original folder
fileList = FileListCapture(originPath, fileType)

for file in fileList:
    # Get last modified date and current date
    modDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    currentDate = datetime.datetime.today()

    filePathList = file.split("\\") # create list from filepath
    filename = filePathList[-1]

    # If modified in the last 24 hours copy to destination
    modifyDateLimit = modDate + datetime.timedelta(days=1)

    # If the file was edited less than 24 hrs ago copy it
    if modifyDateLimit > currentDate:
        shutil.copy2(file, destinationPath + filename)
        
