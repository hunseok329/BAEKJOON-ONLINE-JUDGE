from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

box = []
tomato = []
for _ in range(M):
    box.append(list(map(int,input().split())))
    
for y in range(M):
    for x in range(N):
        if box[y][x] == 1:
            tomato.append([x, y])

def bfs(tomato):
    q = deque(tomato)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    maximum = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and box[ny][nx] == 0:
                q.append([nx, ny])
                box[ny][nx] = box[y][x] + 1
                if box[ny][nx] > maximum:
                    maximum = box[ny][nx]
    for b in box:
        if 0 in b:
            return -1
    return maximum-1

print(bfs(tomato))