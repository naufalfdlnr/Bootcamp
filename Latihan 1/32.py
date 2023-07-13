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