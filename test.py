with open ('9lan.in', 'r') as f:
    n = int(f.readline())
if  n == 0:
    with open ('9lan.out', 'w') as f:
        f.write (str(1))
else:
    if n % 4 == 0:
        with open('9lan.out', 'w') as f:
            f.write(str(6))
    if n % 4 == 1:
        with open('9lan.out', 'w') as f:
            f.write(str(2))
    if n % 4 == 2:
        with open('9lan.out', 'w') as f:
            f.write(str(4))
    if n % 4 == 3:
        with open('9lan.out', 'w') as f:
            f.write(str(8))




