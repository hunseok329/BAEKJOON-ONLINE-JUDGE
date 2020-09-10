from itertools import combinations

n, m = map(int, input().split())

p = list(combinations(range(1,n+1), m))
for i in p:
    print(' '.join(map(str, i)))