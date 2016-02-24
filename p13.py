import numpy as np

f = open('p13.dat', 'r')
DATA = f.readlines()
f.close()

SUM = 0
for x in DATA:
    SUM += int(x)

STRSUM = str(SUM)
print(SUM)
print(STRSUM[:10])
