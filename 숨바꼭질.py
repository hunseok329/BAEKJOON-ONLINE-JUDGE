from collections import deque

x, y = map(int, input().split())

dp = [float('inf')] * 100001

def bfs(arr, start):
    q = deque()
    q.append(start)
    arr[start] = 0
    dx = [-1, 1, 2]

    while q:
        root = q.popleft()

        for i in range(3):
            if i == 2:
                nx = root * dx[i]
            else:
                nx = root + dx[i]

            if 0 <= nx < 100001:
                if arr[nx] > arr[root] + 1:
                    arr[nx] = arr[root] + 1
                    q.append(nx)
    return arr


result = bfs(dp, x)

print(result[y])