import heapq
import sys
num = int(sys.stdin.readline())
result = []
for _ in range(num):
    numbers = int(sys.stdin.readline())
    heapq.heappush(result, numbers) 
for _ in range(num):
    print(heapq.heappop(result))