N, M = map(int, input().split())

maps = []
result = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

for _ in range(N):
    maps.append(list(map(int ,input().split())))
    
def squared(a, b):
    global N
    
    answer = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            for w in range(N):
                answer[i][j] += a[i][w] * b[w][j]
            answer[i][j] %= 1000
    return answer
        
    
def squaredCheck(m):
    global maps, result

      
    if m == 1:
        result = squared(result, maps)
    
    elif m % 2 == 0:
        squaredCheck(m//2)
        result = squared(result, result)
    else:
        squaredCheck(m-1)
        result = squared(maps, result)
        
squaredCheck(M)

for numbers in result:
    for row in numbers:
        print(row, end= ' ')
    print()