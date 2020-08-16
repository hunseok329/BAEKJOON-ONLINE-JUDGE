p = []
for _ in range(10):
    n = int(input())
    num = n % 42
    if num not in p:
        p.append(num)
print(len(p))
