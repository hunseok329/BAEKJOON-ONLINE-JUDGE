# pypy3
numbers = []

n = int(input())
for _ in range(n):
    numbers.append(int(input()))

maximum = max(numbers)

c = [i for i in range(maximum+1)]

c[0] = 0
c[1] = 0

for a in range(2, maximum+1):
    num = a*2
    while num <= maximum:
        c[num] = 0
        num = num + a

checking = []
for w in c:
    if w != 0:
        checking.append(w)
result = 0
for num in numbers:
    for h in checking:
        if h > num//2:
            break
        if num-h in checking:
            result = h
    print(result, num-result)
        