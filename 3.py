def hitung(buah):
    jumlah = {}

    for x in buah:
        if x in jumlah:
            jumlah[x] += 1
        else:
            jumlah[x] = 1

    return jumlah

buah = ["apel", "jeruk", "apel", "mangga", "apel", "jeruk"]
banyak = hitung(buah)

for string, count in hitung():
    print(f"{string}: {count}")