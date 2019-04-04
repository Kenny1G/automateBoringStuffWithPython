import re
def strengthChecker(password):
    (bad) = "Your shit weak homie"
    # capital letter
    capital = re.compile('[A-Z]')
    # digit
    digit = re.compile('\d')
    #lowercase
    lowercase = re.compile('[a-z]')
    if len(password) < 8:
        print (bad)
    elif capital.search(password) == None:
        print (bad)
    elif digit.search(password) == None:
        print (bad)
    elif lowercase.search(password) == None:
        print (bad)
    else:
        print ('Your gucci my dude')
print('STRONG PASSWORD DECIDER')
password = input('put in your password: ')
strengthChecker(password)
