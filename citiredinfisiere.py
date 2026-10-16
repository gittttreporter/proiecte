f = open('nr.in', 'r')
g = open('nr.out', 'w')
a, b = map(int, f.read().split())
s = a + b
g.write(str(s))
f.close()
g.close()