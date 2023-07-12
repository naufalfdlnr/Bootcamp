x = int(input('masukan sebuah angka '))
if x > 1:
    for angka in range(2,x):
        if (x % angka) == 0:
            print('angka bukan bilangan prima ')
            break
        else:
            print('angka bilangan prima')
            break