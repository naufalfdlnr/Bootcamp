jenis_zakat = input("masukan jenis zakat = ")
harga_gram = int(input("masukan harga 1 Gram emas = "))
harta = int(input("masukan nilai harta = "))
haul = input("ya / tidak = ")
total_harta = harga_gram * 85
zakat = harta * 0.025
if haul == "tidak":
        print ("maaf harta anda belum bisa di zakatkan")
if jenis_zakat == "MAL" and haul == "ya":
    if harta >= total_harta:
        print("zakat anda adalah", zakat)
    else:
         print("maaf zakat anda belum bisa di zakatkan")