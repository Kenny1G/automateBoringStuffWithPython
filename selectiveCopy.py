import re,os,shutil
regex = re.compile(r'.*jpg|.*pdf')
folder = 'C:\\Users\\osele\\Pictures\\wallpapers'
for folderName, subFolders,filenames in os.walk(folder):
    for filename in filenames:
        if regex.findall(filename) != []:
            os.chdir(folder)
            file = os.path.abspath(filename)
            shutil.copy(file,'C:\\pythonscripts\\selectiveFolder')
            #print(str(file))
    #print('The current folder is ' + folderName)
    #print('FILE INSIDE ' + folderName + ': '+ filenames)
