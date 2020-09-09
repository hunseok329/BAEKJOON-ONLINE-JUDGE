from itertools import permutations

x, y = map(int, input().split())

p = permutations(range(1, x+1), y)
for i in p:
    print(' '.join(map(str, i)))