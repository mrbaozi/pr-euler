def is_palindrome(s):
    for i in range(int(len(s)/2)):
        if (s[i] != s[-i-1]):
            return False
    return True

pals = []

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        x = i*j
        if is_palindrome(str(x)):
            pals.append(x)

print(max(pals))
