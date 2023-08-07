def skor():
    banyak_klub = int(input())
    data = dict()
    for i in range(banyak_klub):
        klub, play, w, d, l, gm, gk = input().split()
        data[klub] = [int(play), int(w), int(d), int(l), int(gm), int(gk)]
    
    return data

def hitung(a):
    for i, j in a.items():
        point = j[1]*3 + j[2]
        j.append(point)
        a.update({i:j})

    return a

def sort(a):
    sort = sorted(a.items(), key=lambda x: x[1], reverse=True)
    key = list(sort[0])
    return key

def main():
    x = skor()
    x = hitung(x)
    x = sort(x)
    print(x[0])

if __name__ == '__main__':
    main() 
# ARS 38 26 6 6 88 43
# MUN 38 23 6 9 58 43
# NEW 38 19 14 5 68 33
# MCI 38 28 5 5 94 33