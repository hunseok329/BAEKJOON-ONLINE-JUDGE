num = int(input())

n = 1
count = 0

for i in range(num, 0, -1):
    n *= i

for w in str(n)[::-1]:
    if w == "0":
        count += 1
    else:
        break
print(count)