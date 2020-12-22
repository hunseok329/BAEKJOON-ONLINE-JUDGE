import heapq
import sys

num = int(sys.stdin.readline())

hp = []
for _ in range(num):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(hp, (-n, n))
    else:
        if len(hp):
            print(heapq.heappop(hp)[1])
        else:
            print(0)            

