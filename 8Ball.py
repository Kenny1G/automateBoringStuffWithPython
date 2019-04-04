

import random


messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask agian later',
            'Concentrate and ask again later',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful',]

while True:
    print('What troubles you young one (put in nothing to exit)')
    q = input()
    if q == '':
        break
    print(messages[random.randint(0, len(messages) - 1)])
