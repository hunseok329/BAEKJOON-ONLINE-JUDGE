from collections import deque
import sys

input = sys.stdin.readline

num = int(input())

arr = deque()

for _ in range(num):
    order = input().split()
    if order[0] == 'push': arr.append(int(order[1]))
    elif order[0] == 'size': print(len(arr))
    elif order[0] == 'empty':
        print(0 if len(arr) else 1)
    elif order[0] == 'pop':
        print(arr.popleft() if len(arr) else -1)
    elif order[0] == 'front':
        print(arr[0] if len(arr) else -1)
    elif order[0] == 'back':
        print(arr[-1] if len(arr) else -1)