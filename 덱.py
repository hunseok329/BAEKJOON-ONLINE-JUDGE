from collections import deque
import sys

d = deque()

num = int(input())

for _ in range(num):
    orders = sys.stdin.readline().split()
    if orders[0] == 'push_back':
        d.append(int(orders[-1]))
    elif orders[0] == 'push_front':
        d.appendleft(int(orders[-1]))
    elif orders[0] == 'pop_front':
        if len(d): print(d.popleft())
        else: print(-1)
    elif orders[0] == 'pop_back':
        if len(d): print(d.pop())
        else: print(-1)
    elif orders[0] == 'size':
        print(len(d))
    elif orders[0] == 'empty':
        if len(d): print(0)
        else: print(1)
    elif orders[0] == 'front':
        if len(d): print(d[0])
        else: print(-1)
    else:
        if len(d): print(d[-1])
        else: print(-1)