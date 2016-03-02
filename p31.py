from projecteuler_util import memoize

@memoize
def count(N, m):
    if N < 0 or m < 0:
        return 0
    if N == 0:
        return 1
    return count(N, m - 1) + count(N - S[m], m)

S = [1, 2, 5, 10, 20, 50, 100, 200]
print(count(200, 7))
