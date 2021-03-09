import sys
import heapq

input = sys.stdin.readline

T = int(input())

def solution(graph, start):
    distances = [float('inf') for _ in graph]
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])  

    while q:
        weight, destination = heapq.heappop(q)

        if distances[destination] < weight:
            continue

        for new_destination, new_weight in graph[destination]:
            distance = weight + new_weight
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])

    return distances

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[]for _ in range(n+1)]

    check = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    for _ in range(t):
        check.append(int(input()))
    check.sort()
    
    result = solution(graph, s)
    v1 = solution(graph, g)
    v2 = solution(graph, h)
    
    for i in check:
        if result[i] == float('inf'):
            continue
        if result[i] == result[g] + v1[h] + v2[i] or result[i] == result[h] + v2[g] + v1[i]:
            print(i, end=" ")
    print()