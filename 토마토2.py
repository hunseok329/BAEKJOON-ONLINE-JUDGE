from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = []
check = False
tomato = deque()
for _ in range(h):
    temp = []
    for _ in range(n):
        t = list(map(int, input().split()))
        if 0 in t:
            check = True
        temp.append(t)
    box.append(temp)

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                tomato.append([x, y, z])


def bfs(box, tomato):
    dx = [0, 0, 1, -1, 0 ,0]
    dy = [1, -1, 0, 0, 0, 0,]
    dz = [0, 0, 0, 0, 1, -1]
    maximum = 1
    while tomato:
        x, y, z = tomato.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    maximum = box[nz][ny][nx]
                    tomato.append([nx, ny, nz])
    
    for i in range(h):
        for j in range(n):
            if 0 in box[i][j]:
                return -1
    return maximum-1


if check:
    print(bfs(box, tomato))    
else:
    print(0)