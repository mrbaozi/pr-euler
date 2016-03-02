from projecteuler_util import factorial

factorials = [factorial(n) for n in range(10)]

def is_curious(n):
    csum = 0
    for x in str(n):
        csum += factorials[int(x)]
    return True if csum == n else False

solution = 0
for i in range(3, 7 * factorial(9)):
    if is_curious(i):
        print(i)
        solution += i

print("sum = %s" %(solution))
