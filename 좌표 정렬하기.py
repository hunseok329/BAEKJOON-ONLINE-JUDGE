n = int(input())
result = []
for i in range(n):
    result.append(list(map(int, input().split())))
result = sorted(result, key= lambda x : (x[0], x[1]))
for word in result:
    print(word[0], word[1])