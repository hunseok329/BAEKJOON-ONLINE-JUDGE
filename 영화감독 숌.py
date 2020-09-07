num = int(input())
n = 666
result = []
while len(result) <= num:
    if '666' in str(n):
        result.append(n)
    n += 1
print(result[num-1])