n = int(input())
result = []
for _ in range(n):
    result.append(input())
result = list(set(result))
result = sorted(result, key= lambda x:(len(x), x))
for i in result:
    print(i)
