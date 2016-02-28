from projecteuler_util import proper_divisors

L, s = 20162, 0
abn = set()

for n in range(1, L):
    if proper_divisors(n) > n:
        abn.add(n)
    if not any((n-a in abn) for a in abn):
        s += n

print(s)
