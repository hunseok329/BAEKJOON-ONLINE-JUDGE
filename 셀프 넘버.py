numbers = [x for x in range(10000)]

for i in range(10000):
    string = str(i)
    num = i
    for x in string:
        num += int(x)
    if num >= 10000:
        continue
    numbers[num] = 0
for num in numbers:
    if num != 0:
        print(num)