import heapq
import sys

num = int(sys.stdin.readline())

hp = []

for _ in range(num):
    t = int(sys.stdin.readline())
    if t == 0:
        if len(hp):
            print(heapq.heappop(hp))
        else:
            print(0)
    else:
        heapq.heappush(hp, t)