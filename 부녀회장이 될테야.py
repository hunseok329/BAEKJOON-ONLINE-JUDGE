apart = [[1 for x in range(14)]for y in range(15)]

for i in range(1, 14+1):
    apart[0][i-1] = i

for y in range(1, 15):
    for x in range(1, 14):
        apart[y][x] = apart[y-1][x] + apart[y][x-1]
    
num = int(input())
result = []
for _ in range(num):
    k = int(input())
    n = int(input())
    result.append(apart[k][n-1])
for i in result:
    print(i)