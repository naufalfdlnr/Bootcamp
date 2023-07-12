x = input('masukan sebuah kalimat ')
y = x.split()
z = ''
for word in y:
    z = word[0].upper()
print(z)