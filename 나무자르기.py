import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
tree = Counter(map(int, sys.stdin.readline().split()))

start, end = 0, max(tree)

def cut_tree(tree, std):
    sum = 0
    for t, c in tree.items():
        if t > std:
            sum += (t-std) * c
    return sum

while start <= end:
    mid = (start + end) // 2
    
    if cut_tree(tree, mid) >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)