result = 0
for i in range(2, 5 * pow(9, 5)):
    if i == sum([pow(int(x), 5) for x in str(i)]):
        print(i)
        result += i
print("sum = %s" %(result))
