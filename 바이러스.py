N = int(input())
M = int(input())

graph = {}

for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)

def bfs(graph, root):
    visited = []
    q = [root]
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                q += temp
    return visited

print(len(bfs(graph, 1))-1)