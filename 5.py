def divisors(n, showall=True):
    div = 2
    res = []
    while (n > 1):
        if (0 == (n % div)):
            res.append(div)
            n /= div
            div -= 1
        div += 1
    return res if showall else res[-1]

for i in range(2, 21):
    print("%s: %s" %(i, divisors(i)))
