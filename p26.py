from projecteuler_util import is_prime

prime_list = [i for i in range(1000) if is_prime(i)]

for p in prime_list[::-1]:
    period = 1
    while  pow(10, period, p) != 1:
        period += 1
    if p-1 == period:
        break

print(p)
