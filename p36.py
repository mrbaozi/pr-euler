def is_palindrome(s):
    for i in range(int(len(s)/2)):
        if (s[i] != s[-i-1]):
            return False
    return True

solution = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
            print(i)
            solution += i

print("sum = %s" %(solution))
