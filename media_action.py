import os
import inspect
import shutil

PATH = os.path.dirname(os.path.realpath(inspect.stack()[0][1]))


def CopyVideoFiles(source, dest):
    for files in os.listdir(source):
        if files.endswith(".mp4") or files.endswith(".webm") or files.endswith(".ogv"):
            shutil.copy(files,dest)

def CopyVideoFile(source, dest):
    if source.endswith(".mp4") or source.endswith(".webm") or source.endswith(".ogv"):
        shutil.copy(source,dest)
        

def ClearFolder(folder):
    for files in os.listdir(folder):
        filePath = os.path.join(folder, files)
        os.remove(filePath)

def ClearTestFolder():
    testFolder = os.path.join(PATH, "test")
    for files in os.listdir(testFolder):
        os.remove(files)

def MoveTemplateToTest(folder):
    shutil.copytree(folder, os.path.join(PATH, "test"))

def TestHTMLFilePath():
    testFolder = os.path.join(PATH, "test")
    return os.path.join(testFolder, "index.html")

def GetTestIndexFile():
    result = None
    testFolder = os.path.join(PATH, "test")
    if len(testFolder) != 0:
        indexFile = os.path.join(testFolder, "index.html")

        if os.path.isfile(indexFile):
            result = indexFile

    return result




