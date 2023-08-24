import random
from datetime import datetime

data = {} 


def code():
    x = input('Masukan Item Code: ')
    if x in data:
        print("Item Code sudah ada di inventory")
        y = input('Lanjut (Ya/Tidak): ').lower()
        if y == 'ya':
            return code()
        elif y == 'tidak':
            return 'Go back..'
        else:
            print("INVALID")
    elif x == '':
        return x.join(random.choices('0123456789', k=12))
    elif len(x) >= 3 and len(x) < 13:    
        return x
    elif len(x) <= 3 or len(x) > 12:
        print('Char Min 3 and Max 12')
        return code()
    

def name():
    x = input('Masukan Item Name: ')
    return x

def values():
    x = input('Masukan Item Amounts: ')
    try:
        qty = float(x)
        return qty
    except ValueError:
        print(("Amounts harus berupa angka."))
        return values()
        

def desc():
    x = input('Masukan Code Description: ')
    if len(x) >= 3 and len(x) <= 256:    
        return x
    elif len(x) <= 3 or len(x) > 256:
        print('INVALID')
        return code()

def date():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date

def add():
    z = {}
    a = code()
    b = name()
    c = values()
    d = desc()
    e = date()
    z[a] = [b,c,d,e]
    print('Success.')
    return data.update(z)

def update():
    x = input('Masukan Item Code barang: ')
    if x in data.keys():
        while True:
            a = int(input('''
1. Edit Nama
2. Edit Jumlah
3. Edit Deskripsi
4. Go Back
Pilih 1~4: '''))
            for i,j in data.items():
                if a == 1:
                    if i == x:
                        c = input('Nama Barang: ')
                        j[0] = c
                        tgl = date()
                        print(f'Update nama in ({tgl})')
                        return data[x]
                elif a == 2:
                    if i == x:
                        d = values()
                        j[1] = d
                        tgl = date()
                        print(f'Update Jumlah in ({tgl})')
                        return data[x]
                elif a == 3:
                    if i == x:
                        e = input('Deskripsi Barang: ')
                        j[2] = e
                        tgl = date()
                        print(f'Update Jumlah in ({tgl})')
                        return data[x]
                elif a == 4:
                    return 'Go back..'
                else:
                    print('INVALID')
    else:
        print("Item not found.")
        while True:
            y = input('Lanjut (Ya/Tidak): ').lower()
            if y == 'ya':
                return update()
            elif y == 'tidak':
                print('Go back..')
            else:
                print("INVALID")

def delete():
        while True:
            opt = input('Cari Name Item(1) / Kembali(2): ')
            if opt == '1':
                x = input('Masukan Item Code: ')
                if x in data:
                    del data[x]
                    print('Deleted.')
                else:
                    print('Item Code tidak ada')
                    y = input('Lanjut (Ya/Tidak): ').lower()
                    if y == 'ya':
                        return delete()
                    elif y == 'tidak':
                        return 'Go back..'
                    else:
                        print("INVALID")
            elif opt == '2':
                return 'Go back..'
            else:
                print('INVALID')


def search():
        keyword = input('Nama Item: ')
        for x, y in data.items():
            if keyword == y[0]:
                a,b,c,d = y[0],y[1],y[2],y[3]
                print(f'''
Item Code      : {x}
Nama Item      : {a}
Jumlah Item    : {b}
Deskripsi Item : {c}
Add Date       : {d}
''')
                
        else:
            q = input('Lanjut (Ya/Tidak): ').lower()
            if q == 'ya':
                return search()
            elif q == 'tidak':
                    return 'Go Back..'
            else:
                print('INVALID')

def menu():
    while True:
        print(''.center(50, '=')+ '=')
        print('|', 'APLIKASI STOCK INVENTORY'.center(47, ' '), '|')
        print(''.center(50, '=')+ '=')
        print(' ')
        print(' ')
        print(''.center(50, '-') + '-')
        print('|', 'DAFTAR ITEM INVENTARIS'.center(47, ' '), '|')
        print(''.center(50, '-' )+ '-')
        print('|', 'Item Code'.center(11), '|', 'Nama Item'.center(11), '|','Jumlah'.center(6), '|', 'Deskripsi')
        print(''.center(50, '-' )+ '-')
        for x,y in data.items():
            a,b,c,d = y[0],y[1],y[2],y[3]
            print('|',str(x).center(11),'|',str(a).center(11),'|',str(b).center(6),'| ',str(c),f'(Add Date : {str(d)})')
        print(''.center(50, '-' )+ '-')
        print(' ')
        print(' ')
        print('----------------------------------')
        print('|', 'ACTION'.center(30, ' '), '|')
        print('----------------------------------')
        print('| 1. Add                         |')
        print('| 2. Delete                      |')
        print('| 3. Update                      |')
        print('| 4. Search                      |')
        print('| 5. Exit                        |')
        print('----------------------------------')
        print(' ')
        choice = input('Enter your choice: ')
        if choice == '1':
            add()
        elif choice == '2':
            delete()
        elif choice == '3':
            update()
        elif choice == '4':
            search()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("INVALID")

menu()