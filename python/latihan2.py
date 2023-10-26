r = float(input("Masukan Jari2: "))
t = float(input("Masukan Tinggi: "))
price = float(input("Masukan harga 1 Liter: "))
volume = (3.14 * r * r) * t
liter = volume * 0.001
total = liter * price
print("Total uang yang harus dibayar adalah:", total)