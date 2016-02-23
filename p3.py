from projecteuler_util import isqrt, is_prime

def fermat_factor(n, verbose=True):
    a = b = isqrt(n)
    b2 = a*a - n
    while b*b != b2:
        if verbose:
            print("a=%s b2=%s b=%s" % (a, b2, b))
        a += 1
        b2 = a*a - n
        b = isqrt(b2)
    return a+b, a-b

def prime_factor(n):
    while (n%2 == 0) and (n != 2):
        n = int(n/2)
    if is_prime(n):
        return n
    x = fermat_factor(n, False)
    return prime_factor(x[0]), prime_factor(x[1])

print(prime_factor(600851475143))
