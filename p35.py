from projecteuler_util import is_prime

f = open('p27_primes.dat', 'r')
primes = set([int(x) for x in f.readline().split()])
f.close()

primes_set = set(primes)

def circular_prime(n):
    strn = str(n)
    for i in range(len(strn)):
        if (int(strn[i:] + strn[:i])) not in primes:
            return False
    return True

solution = 0
for x in primes:
    if circular_prime(x):
        print(x)
        solution += 1
print("%s circular primes" %(solution))
