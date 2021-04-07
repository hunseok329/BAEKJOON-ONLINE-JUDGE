import sys

input = sys.stdin.readline

total = 0
maximum = 0
for _ in range(4):
    o, i = map(int, input().split())
    total -= o
    total += i
    
    if total > maximum:
        maximum = total
print(maximum)