import re
def strip2(string,*args,**kwargs):
    string2 = kwargs.get('a',None)
    if string2 == None:
        string = string.strip()
        print(string)
    else:
        ge = re.compile(string2)
        string = ge.sub('',string)
        print(string)


text = input('what is your text: ')
remove = input('what do you want to get rid of: ')

strip2(text,a = remove)

input('press enter to exit....')
