import math

def ndivisors(n):
    nod = 0
    root = int(math.sqrt(n))

    for i in range(1, root+1):
        if n%i == 0:
            nod += 2
    if (root**2 == n):
        nod -= 1
    return nod

number = 0
i = 1
while ndivisors(number) < 500:
    number += i
    i += 1

print(number)
