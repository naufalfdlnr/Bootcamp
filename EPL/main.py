from datetime import datetime

q = dict()

with open('..\\stat.txt') as x:
    stat = dict()
    for line in x:
        klub,play,w,d,l,gf,ga,gd,points = line.split()
        stat[klub] = [int(play),int(w),int(d),int(l),int(gf),int(ga),int(gd),int(points)]
        q.update(stat)

def pekan1():
    with open('..\\pekan1.txt') as file:
        h = 1
        for line2 in file:
            print(f'Match {h}')
            h += 1
            klub1,klub2 = line2.split()
            a = int(input(f'Goals {klub1}: '))
            b = int(input(f'Goals {klub2}: '))
            if klub1 > klub2:
                for c,d in q.items():
                    if c == klub1:
                        d[0] += 1
                        d[1] += 1
                        d[7] += 3
                        d[4] += a
                        d[5] += b
                        d[6] = d[4] - d[5]
            elif klub1 < klub2:
                for c,d in q.items():
                    if c == klub2:
                        d[0] += 1
                        d[1] += 1
                        d[7] += 3
                        d[4] += b
                        d[5] += a
                        d[6] = d[4] - d[5]
            else:
                for c,d in q.items():
                    if c == klub1:
                            d[0] += 1
                            d[2] += 1
                            d[7] += 1
                            d[4] += a
                            d[5] += a
                            d[6] = d[4] - d[5]
                    if c == klub2:
                            d[0] += 1
                            d[2] += 1
                            d[7] += 1
                            d[4] += b
                            d[5] += b
                            d[6] = d[4] - d[5]
        while True:
            save1 = input('Save/No: ').lower()
            if save1 == 'save':
                save()
                return
            elif save1 == 'no':
                return   
            else:
                print('INVALID') 

def pekan2():
    with open('D:\\nopal\\Pa Bunyamin\\TUGAS 10\\latihan\\EPL\\pekan1.txt') as file:
        h = 1
        for line2 in file:
            print(f'Match {h}')
            h += 1
            klub1,klub2 = line2.split()
            a = int(input(f'Goals {klub1}: '))
            b = int(input(f'Goals {klub2}: '))
            if klub1 > klub2:
                for c,d in q.items():
                    if c == klub1:
                        d[0] += 1
                        d[1] += 1
                        d[7] += 3
                        d[4] += a
                        d[5] += b
                        d[6] = d[4] - d[5]
            elif klub1 < klub2:
                for c,d in q.items():
                    if c == klub2:
                        d[0] += 1
                        d[1] += 1
                        d[7] += 3
                        d[4] += b
                        d[5] += a
                        d[6] = d[4] - d[5]
            else:
                for c,d in q.items():
                    if c == klub1:
                            d[0] += 1
                            d[2] += 1
                            d[7] += 1
                            d[4] += a
                            d[5] += a
                            d[6] = d[4] - d[5]
                    if c == klub2:
                            d[0] += 1
                            d[2] += 1
                            d[7] += 1
                            d[4] += b
                            d[5] += b
                            d[6] = d[4] - d[5]
        while True:
            save1 = input('Save/No: ').lower()
            if save1 == 'save':
                save()
                return
            elif save1 == 'no':
                return   
            else:
                print('INVALID') 
    
def save():
    with open('D:\\nopal\\Pa Bunyamin\\TUGAS 10\\latihan\\EPL\\stat.txt', 'w') as x:
        for a,b in q.items():
            x.write(f'{a} {str(b[0])} {str(b[1])} {str(b[2])} {str(b[3])} {str(b[4])} {str(b[5])} {str(b[6])} {str(b[7])}\n')

def tanding():
    while True:
        a = input('Masukan Pekan/Back: ').lower()
        if a == '1':
            pekan1()
        elif a == '2':
            pekan2()
        elif a == 'back':
            return
        else:
            print('INVALID')
            

def match():
    while True:
        x = input('Match/Menu: ').lower()
        if x == 'match':
            tanding()
        elif x == 'menu':
            return
        else:
            print("INVALID")

def tambah():
    klub = input('Masukan Nama Klub Dengan 3 Huruf: ').upper()
    if len(klub) != 3:
        print('INVALID')
        return tambah()
    while True:
        play = int(input('Masukan Jumlah Permainan: '))
        w = int(input('Masukan Jumlah Menang: '))
        d = int(input('Masukan Jumlah Imbang: '))
        l = int(input('Masukan Jumlah Kalah: '))
        if play < (w+d+l):
            print('Jumlah Kemenangan,Imbang dan Kalah Harus Sesuai Dengan Jumlah Permainan.')
        else:
            gf = int(input('Masukan Jumlah Gol: '))
            ga = int(input('Masukan Jumlah Kemasukan: '))
            points = w*3 + d
            gd = gf - ga
            data = {klub : [play,w,d,l,gf,ga,gd,points]}
            q.update(data)
            print('Data Berhasil Di Tambahkan.')
            return
        
def ubah():
    klub = input('Masukan Nama Klub: ').upper()
    if klub in q.keys():
        while True:
            menu = int(input('''
1. Ubah Banyak Permainan Kemenangan,Imbang dan Kalah
2. Ubah Banyak Gol dan Kemasukan
0. Kembali

Pilih (1/2/0): '''))
            for a,b in q.items():
                if menu == 1:
                    if a == klub:
                        while True:
                            play = int(input('Masukan Jumlah Permainan: '))
                            w = int(input('Masukan Jumlah Menang: '))
                            d = int(input('Masukan Jumlah Imbang: '))
                            l = int(input('Masukan Jumlah Kalah: '))
                            b[0] = play
                            b[1] = w
                            b[2] = d
                            b[3] = l
                            if play < (w+d+l):
                                print('Jumlah Kemenangan,Imbang dan Kalah Harus Sesuai Dengan Jumlah Permainan.')
                            else:
                                b[7] = w*3 + d
                                print('Berhasil Di Ubah.')
                                break
                elif menu == 2:
                    if a == klub:
                        gf = int(input('Masukan Jumlah Gol: '))
                        ga = int(input('Masukan Jumlah Kemasukan: '))
                        gd = gf - ga
                        b[4] = gf
                        b[5] = ga
                        b[6] = gd
                        print('Berhasil Di Ubah.')
                        break
                elif menu == 0:
                    print('Kembali..')
                    return
                else:
                    print("INVALID")                 
    else:
        print("Klub Tidak Ada.")
        while True:
            y = input('Lanjut (Ya/Tidak): ').lower()
            if y == 'ya':
                return ubah()
            elif y == 'tidak':
                print('Kembali..')
                return
            else:
                print("INVALID")
 
def hapus():
    while True:
        klub = input('Masukan Nama Club: ').upper()
        if klub in q:
            del q[klub]
            print('Deleted..')
            return
        else:
            print("Klub Tidak Ada.")
            while True:
                y = input('Lanjut (Ya/Tidak): ').lower()
                if y == 'ya':
                    return hapus()
                elif y == 'tidak':
                    print('Kembali..')
                    return
                else:
                    print("INVALID")

def menu():
    while True:
        w = {k: v for k, v in sorted(q.items(), key=lambda item: item[1], reverse=True)}
        print(''.center(119, '-'))
        print('EPL'.center(117, ' '))
        print(''.center(119, '-' ))
        print('Position'.center(10), 'Club'.center(10),'Played'.center(10), 'Won'.center(10),'Draw'.center(10),'Lost'.center(10),'GF'.center(10),'GA'.center(10),'GD'.center(10),'Points'.center(10))
        print(''.center(119, '-' ))
        i = 1
        for x,y in w.items():
            a,b,c,d,e,f,g,h = y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7]
            print(f'{i}'.center(10), str(x).center(10),str(a).center(10),str(b).center(10),str(c).center(10),str(d).center(10),str(e).center(10),str(f).center(10),str(g).center(10),str(h).center(10))
            i += 1
        print(''.center(119, '-' ))
        print(' ')
        print(' ')
        print('----------------------------------')
        print('|', 'ACTION'.center(30, ' '), '|')
        print('----------------------------------')
        print('| 1. Add Club                    |')
        print('| 2. Edit Club                   |')
        print('| 3. Del Club                    |')
        print('| 4. Match Club                  |')
        print('| 5. Save                        |')
        print('| 0. Exit                        |')
        print('----------------------------------')
        print(' ')
        choice = input('Enter your choice: ')
        if choice == '1':
            tambah()
        elif choice == '2':
            ubah()
        elif choice == '3':
            hapus()
        elif choice == '4':
            match()
        elif choice == '5':
            print('Saved.')
            save()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("INVALID")

    
menu()
