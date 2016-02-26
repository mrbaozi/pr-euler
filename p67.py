# This is the same solution as Problem 18

f = open('p67.dat', 'r')
DAT = f.readlines()
f.close()

STRDAT = [] * len(DAT)

for x in DAT:
    STRDAT.append(x.split())

INTDAT = [[int(i) for i in STRDAT[j]] for j in range(len(STRDAT))]

INTDAT_REVERSE = list(reversed([list(row) for row in INTDAT]))

for i in range(len(INTDAT_REVERSE) - 1):
    for j in range(0, len(INTDAT_REVERSE[i]) - 1):
        INTDAT_REVERSE[i+1][j] += max(INTDAT_REVERSE[i][j:j+2])

print(INTDAT_REVERSE[-1])
