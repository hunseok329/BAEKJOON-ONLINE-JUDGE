numbers = []

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)
    
maximum = max(numbers)*2
c = [True for x in range(maximum+1)]
c[0] = False
c[1] = False

for i in range(2, maximum+1):
    n = i*2
    while n <= maximum:
        c[n] = False
        n = n + i

for i in numbers:
    count = 0
    for a in range(i+1, i*2+1):
        if c[a] == True:
            count += 1
    print(count)