import sys
input = sys.stdin.readline

n = int(input())

loaps = list()

for _ in range(n):
    loaps.append(int(input()))
    
loaps.sort(reverse=True)

max_num = 0

for x in range(n):
    temp = loaps[x] * (x + 1)
    if temp >= max_num:
        max_num = temp

print(max_num)