#take number, check if number even or odd do ting depending on result
def collatz(userNumber):
    if userNumber % 2 == 1:
        userNumber = userNumber * 3 + 1
    else:
        userNumber = userNumber // 2
    print(userNumber)
    return userNumber
while True:
    try:
        print('input a number please')
        i = int(input())
        while i != 1:
            i = collatz(i)
        break
    except ValueError:
        print('it has to be an integer', end = ', ')

    


    
    
    
    
