x = 9
y = 0
z = 4
while y < z:
    guess = int(input('guess number.. '))
    y += 1
    if guess == 9:
        print('u won..')
    if guess != 9 and y <= 3:
        print('try again')