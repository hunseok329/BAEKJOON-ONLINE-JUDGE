import itertools
n,maximum = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
for i in itertools.combinations(numbers, 3):
    if sum(i) <= maximum:
        result.append(sum(i))
print(max(result))