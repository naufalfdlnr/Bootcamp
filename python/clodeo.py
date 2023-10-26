nilai_transaksi = int(input())
metode_pembayaran = input("VA / QRIS = ")
if metode_pembayaran == "VA":
    nilai_transaksi < 500000
    total = nilai_transaksi + 4500
    if nilai_transaksi > 500000:
        total = nilai_transaksi
    if  nilai_transaksi < 10000:
        total = ("MAAF TRANSAKSI TIDAK DAPAT KURANG DARI 10000")
if metode_pembayaran == "QRIS":
    500000 > nilai_transaksi > 2000000
    total = nilai_transaksi + nilai_transaksi * 0.007
    if nilai_transaksi < 500000:
        total = nilai_transaksi
    if nilai_transaksi > 2000000:
        total = ("MAAF TRANSAKSI TIDAK DAPAT LEBIH DARI 2000000")
print(total)


