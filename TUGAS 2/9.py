angka = int(input("Masukkan angka: "))
a, b = 0, 1
while b < angka:
    a, b = b, a + b
if b == angka:
    hasil = 1
    print("Angka tersebut adalah bilangan Fibonacci")
else:
    hasil = 0
    print("Angka tersebut bukan bilangan Fibonacci")


        