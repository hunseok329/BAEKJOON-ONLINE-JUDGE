import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

maps = [i for i in range(n+1)]

ans = 1

def find(x):
    if x == maps[x]:
        return x
    maps[x] = find(maps[x])
    return maps[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        maps[b] = a
    else:
        maps[a] = b
        
flag = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    
    if find(a) == find(b):
        flag += 1
        break
    else:
        union(a, b)
        ans += 1

if flag == 0 and ans == m+1:
    ans = 0
print(ans)