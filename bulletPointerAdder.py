#bulletPointerAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip,re
text = pyperclip.paste()
splitter = re.compile('\d:')
#TODO: seperate lines and add starsself.
#Seperate lines and add stars
lines =  re.split(splitter,text)
for i in range(len(lines)):  #loop through all indexes in the "lines" list
    lines[i] = '# ' + lines[i]#add # to each string in "lines" list
text = ''.join(lines)
pyperclip.copy(text)
