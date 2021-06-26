n = int(input())

cost = list(map(int, input().split()))

maps = [[0 for _ in range(n+1)] for _ in range(n+1)]

for y in range(1, n+1):
    for x in range(1, n+1):
        maps[y][x] = max(maps[y][x-1], maps[y-1][x])
        
        if y == x:
            maps[y][x] = max(maps[y][x], cost[y-1])
        if y < x:
            maps[y][x] = max(maps[y][x], maps[y][x-y] + cost[y-1])            

print(maps[-1][-1])