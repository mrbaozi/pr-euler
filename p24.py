from projecteuler_util import factorial

def get_perm(input_list, p):

    perm_solved = []
    perm_digits = list(input_list)

    for n in range(len(perm_digits), 0, -1):
        total_perms = factorial(n)

        if p > total_perms:
            print("Permutation %s does not exist." %(p))
            return

        line = total_perms / n
        r = p % line

        if r > 0 and r <= total_perms:
            x = (p - r) / factorial(n - 1)

        else:
            x = (p - (n - 1)) / factorial(n - 1)

        p = int(p % line)
        perm_solved.append(perm_digits.pop(int(x)))

    return perm_solved

print(get_perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
