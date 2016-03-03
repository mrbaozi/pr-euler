from projecteuler_util import is_prime

def is_truncatable(n):
    if n < 10:
        return False
    for i in range(1, len(str(n))):
        if not int(str(x)[:-i]) in primes or not int(str(x)[i:]) in primes:
            return False
    return True

f = open('p27_primes.dat', 'r')
primes = set([int(x) for x in f.readline().split()])
f.close()

solution = 0
for x in primes:
    if is_truncatable(x):
        print(x)
        solution += x

print("sum = %s" %(solution))
