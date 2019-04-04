#! python
# renameDates.py - Renames filenames with American MM-DD-YY date format
# to European DD-MM-YY

import os,re,shutil

#Create a regex that matches files with the american date format
datePattern = re.compile(r""" ^(.*?) # all text before the date
        ((0|1)?\d) -                 # one or two digits beginning with one or zero for day
        ((0|1|2|3)?\d)-              # one or two digits starting with 0 1 2 or 3 for month
        ((19|20)\d\d)                # four digits for date
        (.*?)$                      # all text after the date
        """, re.VERBOSE)

#TODO: Loop over the files in the working directory
for MuricaFileName in os.listdir('.'):
    date = datePattern.search(MuricaFileName)
    #Skip files without a date\
    if date = None:
        continue
    #Get the different parts of the filenames
    before  = date.group(1)
    month   = date.group(2)
    day     = date.group(4)
    year    = date.group(6)
    after   = date.group(8)
    #Form the European-style filename.
    EuFileNames = before + day + '-' + month + '-' + year + after
    #Get the full, absolute file paths.
    directoryPath = os.abspath('.')
    MuricaFileName = os.joinpath(directoryPath,MuricaFileName)
    EuFileNames = os.joinpath(directoryPath,EuFileNames)
    #Rename the files.
    print ('Renaming "%s" to  "%s"...' %(MuricaFileName, EuFileNames))
    #shutil.move(MuricaFileName,EuFileNames)    
