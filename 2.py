x = {"Lemari" : input().split()}
a = input()
if a in x.values():
    x.popitem(a)

print(x)