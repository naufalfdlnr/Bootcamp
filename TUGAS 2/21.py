x = int(input('sebutkan angka: '))
a, b= 0, 1
while b < x:
    a, b = b, a + b
if b == x:
    print("Angka tersebut adalah bilangan Fibonacci")
else:
    print("Angka tersebut bukan bilangan Fibonacci")