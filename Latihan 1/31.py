r = float(input('jari": '))
t = float(input('tinggi :'))
harga = float(input('harga per liter: '))
PI = 3.14
volume = PI * r**2 * t
liter = volume * 0.001
bayar = liter * harga
print('banyaknya liter', liter, 'jumlah yang harus di bayar', bayar)
