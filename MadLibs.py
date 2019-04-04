import re
#TODO: get name of text file from user and read it
fileName = input('What is the name of your file: ')
fileText = fileName + '.txt'
file = open(fileText)
fileContent = file.read()
#TODO:create regex for the mad libs
stuffs = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
strings = stuffs.findall(fileContent)
print (strings)
newFile = open(fileText + 'New.txt','w')
for string in strings:
    newRe = re.compile(string)
    current = input('Enter a/an ' + string.lower() + ': ')
    fileContent = newRe.sub( current,fileContent)
    newFile.write(fileContent)
print(fileContent)
