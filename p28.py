diagonals = [1, 1, 1, 1]
index = 0
diagonals_sum = 1       # 1 in the middle of the box
n = 4 * 500             # each half-diagonal has 500 elements; there are 4 half-diagonals

for i in range(2, 2*n + 2, 2):
    if index % 4 == 0:
        index = 0
    diagonals[index] += i
    diagonals_sum += diagonals[index]
    index += 1

print(diagonals)
print(diagonals_sum)
