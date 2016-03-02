from fractions import Fraction

solution = 1
for i in range(10, 99):
    for j in range(i + 1, 100):
        frac = Fraction(i, j)
        if int(str(j)[-1]) != 0 and int(str(i)[-1]) == int(str(j)[0]):
            test = Fraction(int(str(i)[0]), int(str(j)[-1]))
            if frac == test:
                print("%s / %s = %s / %s" %(i, j, str(i)[0], str(j)[-1]))
                solution *= test

print("denominator of product: %s" %(solution.denominator))
