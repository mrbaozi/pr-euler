def is_pandigital(a, b):
    strAll = str(a) + str(b) + str(a * b)    
    if str(0) in strAll:
        return False
    if len(strAll) != 9:
        return False
    if len(set(strAll)) != 9:
        return False
    return True

solution = []
for i in range(2, 100):
    for j in range(int(10000 / i)):
        if is_pandigital(i, j):
            solution.append(i * j)

print(sum(set(solution)))
