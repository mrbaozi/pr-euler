from projecteuler_util import is_prime

S = 2
for i in range(3, 200, 2):
    if is_prime(i):
        S += i
print(S)
