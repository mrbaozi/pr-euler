import string

f = open('p22.dat', 'r')
s = f.read()
f.close()

s = s.strip().split(",")

for i in range(len(s)):
    s[i] = s[i].strip('"')

names = sorted(s)
name_value = []
name_score = []

for i in range(len(names)):
    tmp = 0
    for char in names[i]:
        tmp += string.ascii_uppercase.index(char) + 1
    name_value.append(tmp)
    name_score.append(tmp*(i+1))

print(sum(name_score))
