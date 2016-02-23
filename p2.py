a = 1
b = 0
c = 0
s = 0
while (a+b < 4000000):
    c = a+b
    if (c%2 == 0):
        s += c
    b = a
    a = c
print(s)
