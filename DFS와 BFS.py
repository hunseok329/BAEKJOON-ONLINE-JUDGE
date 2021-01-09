def dfs(v):
    print(v, end=' ')
    visit[v] = True
    for i in range(1, N+1):
        if visit[i] == False and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    q = [v]
    visit[v] = False
    
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if visit[i] == True and matrix[v][i] == 1:
                q.append(i)
                visit[i] = False
                
N, M, V = map(int, input().split())

matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

visit = [False] * (N+1)    

dfs(V)
print()
bfs(V)