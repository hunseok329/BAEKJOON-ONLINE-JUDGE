t = input()

t = t.replace('()', 'r')

total = 0
p = 0

for i in t:
    if i == 'r' and p != 0:
        total += p
    elif i == '(':
        p += 1
    elif i == ')':
        total += 1
        p -= 1

print(total)