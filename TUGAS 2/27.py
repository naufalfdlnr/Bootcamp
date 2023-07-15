x = int(input('masukan angka: '))
a, b = 0, 1
while b < x:
    a, b = b, a + b
if b != x:
    print('angka adalah bilangan fabonacci')
else:
    print('angka bukan bilangan fabonacci')