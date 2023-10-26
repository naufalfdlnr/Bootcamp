y = False
while True:
    x = input('> ').lower()
    if x == 'start':
        if y:
            print('car has alredy started')
        else:
            y = True
            print('starting car')
    elif x == 'stop':
        if not y:
            print('car alredy stoped')
        else:
            y = False
            print('stopped car')
    elif x == 'quit':
        break
    elif x == 'help':
        print('''
start - start a car
stop  - stopping a car
quit  - exit the game''')
    else:
        print('i dont understand')
        