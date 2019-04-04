spam = ['apples', 'bananas','tofu','cats']
finish = ''

def stringer(list):
    global finish
    q = len(list)
    for i in range(q):
        if i == q - 1:
            break
        finish += list[i] + ','
    if q > 1:
        finish += 'and '
    finish += list[q-1]
    return finish

finale = stringer(spam)
print(finale)





        
