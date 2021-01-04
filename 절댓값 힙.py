import heapq
import sys
num = int(sys.stdin.readline())

hp = []

for _ in range(num):
    temp = int(sys.stdin.readline())
    if temp != 0:
        heapq.heappush(hp, (abs(temp), temp))
    else:
        if len(hp):
            n = heapq.heappop(hp)
            print(n[1])
        else:
            print(0)