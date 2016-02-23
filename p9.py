from math import ceil

for i in range(1, 332):
    for j in range(i+1, int(ceil(1000-i)/2)):
        k = 1000 - i - j
        if (i*i + j*j == k*k):
            print(i*j*k)
