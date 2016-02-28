from projecteuler_util import proper_divisors

amicable_numbers = []
for n in range(10000):
    x = proper_divisors(n)
    y = proper_divisors(x)
    if (y == n) and (x != y):
        amicable_numbers.append(n)

print("amicable numbers:\n%s" %(amicable_numbers))
print("sum: %s" %(sum(amicable_numbers)))
