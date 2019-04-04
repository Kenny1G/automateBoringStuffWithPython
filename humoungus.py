#walk through a folder tree.
#find large files > 100mb
#pirnt filed abs path
folder = 'C:\\Users\\osele\\Videos\\Movies'
import os
for folderName, subFolders, fileNames in os.walk(folder):
    os.chdir(folderName)
    for filename in fileNames:
        filepath = os.path.abspath(filename)
        filesize = os.path.getsize(filepath)
        if filesize > 100000000:
            print('File:' + filepath +' \n')
