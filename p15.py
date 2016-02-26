def factorial(n):
    if (n == 1) or (n == 0):
        return 1
    return n*(factorial(n - 1))

def binomial(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

print(binomial(20*2, 20))
