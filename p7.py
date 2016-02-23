from projecteuler_util import is_prime

n = i = 1
while i < 10001:
    n += 2
    if is_prime(n):
        i += 1
print(n)
