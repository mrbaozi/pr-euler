from projecteuler_util import is_prime

def quadratic(n, a=1, b=1):
    return n*n + a*n + b

f = open('p27_primes.dat', 'r')
primes = set([int(x) for x in f.readline().split()])
f.close()

pos_primes = [x for x in range(1000) if x in primes]
neg_primes = [-x for x in pos_primes]
check_primes = neg_primes + pos_primes
aMax, bMax, nMax = 0, 0, 0

for a in check_primes:
    for b in check_primes:
        n = 0
        while is_prime(quadratic(n, a, b)):
            n += 1
        if n > nMax:
            aMax = a
            bMax = b
            nMax = n

print("n*n + (%s)*n + (%s)" %(aMax, bMax))
print("Sequence length: %s" %(nMax))
print("a * b = %s" %(aMax * bMax))
