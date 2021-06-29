from collections import deque
import sys

input = sys.stdin.readline

def bfs(r, maps):
    root = deque([r])

    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, 1, -1, -1, 1]
    
    while root:
        y, x = root.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < w and 0 <= ny < h:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    root.append([ny, nx])           

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    maps = []
    
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    
    total = 0
    
    for y in range(h):
        for x in range(w):
            if maps[y][x] == 1:
                maps[y][x] = 0
                bfs([y, x], maps)
                total += 1
    print(total)