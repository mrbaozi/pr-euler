def digit_sum(n):
    s = 0
    for x in str(n):
        s += int(x)
    return s

print(digit_sum(2**1000))
