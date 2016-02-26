def proper_divisors(n):
    sum = 0
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            sum += i
    return sum

amicable_numbers = []
for n in range(10000):
    x = proper_divisors(n)
    y = proper_divisors(x)
    if (y == n) and (x != y):
        amicable_numbers.append(n)

print("amicable numbers:\n%s" %(amicable_numbers))
print("sum: %s" %(sum(amicable_numbers)))
