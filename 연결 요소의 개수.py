import sys
from collections import deque

input = sys.stdin.readline().rstrip

n, m = map(int, input().split())

graph = {node : [] for node in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

visited = [0 for _ in range(n+1)]

def bfs(start, graph):
    q = deque([start])
    while q:
        root = q.popleft()
        visited[root] = 1
        for i in graph[root]:
            if visited[i] != 1:
                q.append(i)

for i in range(1, n+1):
    if visited[i] != 1:
        bfs(i, graph)
        cnt += 1

print(cnt)