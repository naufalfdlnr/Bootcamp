def pi(x):
    b = tuple(map(int, input('banyak orng per gerbong: ').split()))
    c = 0
    for y in b:
        if y > x:
           c += (y - x)
    return c

print(pi(int(input('max per gerbong: '))))