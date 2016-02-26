f = open('p18.dat', 'r')
DAT = f.readlines()
f.close()

STRDAT = [] * len(DAT)

for x in DAT:
    STRDAT.append(x.split())

INTDAT = [[int(i) for i in STRDAT[j]] for j in range(len(STRDAT))]


# This method always chooses the highest reachable number, which doesn't yield the highest possible sum
# LCOPY = [list(row) for row in INTDAT]
# maxsum = LCOPY[0][0]

# for current_line in range(1, len(LCOPY)):
#     current_max = max(LCOPY[current_line])
#     max_index = LCOPY[current_line].index(current_max)
#     maxsum += current_max

#     for i in range(current_line, len(LCOPY)):
#         LCOPY[i].pop(0) if max_index else LCOPY[i].pop()


# Traverse the list in reverse order, always producing the highest possible sum in the next row.
# This solution should be efficient enough for Problem 67.
INTDAT_REVERSE = list(reversed([list(row) for row in INTDAT]))

for i in range(len(INTDAT_REVERSE) - 1):
    for j in range(0, len(INTDAT_REVERSE[i]) - 1):
        INTDAT_REVERSE[i+1][j] += max(INTDAT_REVERSE[i][j:j+2])

print(INTDAT_REVERSE[-1])
