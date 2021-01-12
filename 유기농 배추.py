num = int(input())

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = [[x, y]]
    graph[y][x] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(graph[0]) or ny >= len(graph):
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                q.append([nx, ny])
                graph[ny][nx] = 0
    return True

def main(m, n, k):
    graph = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                if bfs(graph, x, y):
                    count += 1
    print(count)

for _ in range(num):
    M, N, K = map(int, input().split())
    main(M,N,K)