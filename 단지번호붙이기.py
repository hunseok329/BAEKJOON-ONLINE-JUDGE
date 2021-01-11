num = int(input())

graph = []

for _ in range(num):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0 ,0]
dy = [0, 0, 1, -1]

ans = []

def bfs(x, y, graph):
    queue = [[x, y]]
    graph[y][x] = 0
    count = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= num or ny >= num:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                queue.append([nx, ny])
                count += 1
                graph[ny][nx] = 0
    return count

for y in range(num):
    for x in range(num):
        if graph[y][x] == 1:
            ans.append(bfs(x, y, graph))

print(len(ans))
ans.sort()
for i in ans:
    print(i)