from itertools import product

n, m = map(int, input().split())

p = list(product(range(1,n+1), repeat=m))
for i in p:
    print(' '.join(map(str, i)))