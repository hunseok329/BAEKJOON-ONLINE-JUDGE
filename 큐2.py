from collections import deque
import sys

q = deque()

n = int(input())

for _ in range(n):
    p = sys.stdin.readline().rstrip().split()
    if p[0] == 'push': 
        q.append(int(p[-1]))
    elif p[0] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif p[0] == 'size':
        print(len(q))
    elif p[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif p[0] == 'front':
        if q: print(q[0]
        else: print(-1)
    else:
        if q: print(q[-1])
        else: print(-1)
            