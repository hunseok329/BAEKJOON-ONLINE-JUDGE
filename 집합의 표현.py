import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

num_set = [x for x in range(n+1)]

def find(target):
    if target == num_set[target]:
        return target
    num_set[target] = find(num_set[target])
    return num_set[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        num_set[b] = a
    else:
        num_set[a] = b

for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)