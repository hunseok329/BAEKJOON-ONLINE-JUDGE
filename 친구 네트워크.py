import sys

input = sys.stdin.readline

t = int(input())

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])

for _ in range(t):
    num = int(input())
    parent = dict()
    number = dict()

    for _ in range(num):  
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)