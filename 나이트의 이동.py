from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

def bfs(length, x, y, e_x, e_y):
    matrix = [[0]*length for _ in range(length)]
    q = deque()
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    count = 0
    q.append([x, y, count])
    while q:
        x, y, count = q.popleft()
        if x == e_x and y == e_y:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < length and 0<= ny < length and matrix[ny][nx] == 0:
                q.append([nx, ny, count+1])
                matrix[ny][nx] = 1

for _ in range(T):
    length = int(input())
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())

    print(bfs(length, s_x, s_y, e_x, e_y))