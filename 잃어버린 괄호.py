num = input().split('-')
result = 0
for x in num[0].split('+'):
    result += int(x)
for x in num[1:]:
    for z in x.split('+'):
        result -= int(z)
print(result)