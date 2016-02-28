# Using the "fast doubling" Fibonacci algorithm.

def fib(n):
    if n < 0:
        return
    return _fib(n)[0]

def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2*b - a)
        d = a*a + b*b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c+d)

i = 1
while True:
    if not len(str(fib(i))) < 1000:
        break
    i += 1

print("i = %s" %(i))
