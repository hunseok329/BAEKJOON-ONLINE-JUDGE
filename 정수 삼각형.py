num = int(input())

numbers= []
for _ in range(num):
    numbers.append(list(map(int, input().split())))

for i in range(num-1, 0, -1):
    for j in range(len(numbers[i])-1):
        if numbers[i][j] >= numbers[i][j+1]:
            numbers[i-1][j] += numbers[i][j]
        else:
            numbers[i-1][j] += numbers[i][j+1]
print(numbers[0][0])