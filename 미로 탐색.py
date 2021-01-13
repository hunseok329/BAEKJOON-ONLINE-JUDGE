N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    queue = [[x, y]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                cnt += 1
                queue.append([nx, ny])
    
dfs(0,0)

print(graph[N-1][M-1])