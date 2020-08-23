import os
import shutil


def CopyVideoFiles(source, dest):
    for files in os.listdir(source):
        if files.endswith(".mp4") or files.endswith(".webm") or files.endswith(".ogv"):
            shutil.copy(files,dest)

def CopyVideoFile(source, dest):
    if source.endswith(".mp4") or source.endswith(".webm") or source.endswith(".ogv"):
        shutil.copy(source,dest)
        

def ClearFolder(folder):
    for files in os.listdir(folder):
        os.remove(files)

