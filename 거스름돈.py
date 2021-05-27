n = 1000 - int(input())

result = 0

coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    if n == 0:
        break
    if n >= c:
        d, n = divmod(n, c)
        result += d
print(result)