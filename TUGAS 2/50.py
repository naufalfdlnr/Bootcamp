x = int(input('masukan angka: '))
y = 0
z = x
while z > 0:
    angka = z % 10
    y += angka ** 3
    z //= 10

if x == y:
    print('angka adalah bilangan armstrong')
else:
    print('angka bukan bilangan armstrong')