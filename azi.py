z, l, a = map(int, input().split())
c = int(input())
s = c // 10 ** 12
an = (c // 10 ** 10)
luna = (c // 10 ** 8) % 100
zi = (c // 10 ** 6) % 100

if s == 1 or s == 2:
    if luna < l:
        print("major", a - (1900 + an))
    else:
        if zi < z:
            print("major", a - (1900 + an) - 1)
        else:
            print("major", a - (1900 + a))
else:
    if luna < l:
        print("major", a - (2000 + an))
    else:
        if zi < z:
            print("major", a - (2000 + an) - 1)
        else:
            print("major", a - (2000 + a))