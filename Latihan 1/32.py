liter = float(input('masukan total liter: '))
harga_perliter = float(input('masukan harga per liter: '))
tahu = float(input('masukan ukuran tahu: '))
margin = float(input('masukan jumlah presentase margin: '))
persentase = margin / 100
total_tahu = liter * 1000 / tahu**3
sisa_susu = total_tahu % 1 * tahu**3 * 0.001
biaya_prod = liter * harga_perliter
biaya_prod_pertahu = biaya_prod / total_tahu
harga_jual = biaya_prod_pertahu + (biaya_prod_pertahu * persentase)
print('total tahu yang di hasilkan sebanyak: ', int(total_tahu))
print('sisa susu kedelai: ', '{:.3f}'.format(sisa_susu))
print('total biaya prod: ', biaya_prod)
print('biaya prod per tahu: ', biaya_prod_pertahu)
print('harga jual dengan margin 30%: ', harga_jual)
y = 0
z = 4
while y < z:
    penjualan_tahu = int(input('banyaknya tahu yang ingin di jual 60%: '))   
    if penjualan_tahu >= 60:
        break
presentase_penjualan = penjualan_tahu / 100
a = presentase_penjualan * total_tahu * biaya_prod_pertahu
omset = presentase_penjualan * total_tahu * harga_jual
keuntungan = omset - a
print('total omset pak uu: ', omset)
print('keuntungan pak uu: ', keuntungan)