n = int(input())
result = []
for i in range(n):
    result.append(list(map(int, input().split())))
result = sorted(result, key = lambda x:x[0])
result = sorted(result, key = lambda x:x[1])
for a,b in result:
    print(a, b)