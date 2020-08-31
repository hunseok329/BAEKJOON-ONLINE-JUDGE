num = int(input())
result = []
for _ in range(num):
    n = int(input())
    result.append(n)
result.sort()
for i in result:
    print(i)