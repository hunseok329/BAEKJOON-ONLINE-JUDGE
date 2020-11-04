n, k = map(int, input().split())

p = [x for x in range(1, n+1)]
result = []
num = k

for _ in range(n):
    while num > len(p):
        num -= len(p)
    result.append(str(p.pop(num-1)))
    num += k-1
result = ", ".join(result)
print('<' + result + '>')
        