n = int(input())
numbers = []

for _ in range(n):
    numbers.append(list(map(int, input().split())))

for i in range(1, n):
        for j in range(3):
            if j == 0:
                numbers[i][j] += min(numbers[i-1][1], numbers[i-1][2])
            elif j == 1:
                numbers[i][j] += min(numbers[i-1][0], numbers[i-1][2])
            else:
                numbers[i][j] += min(numbers[i-1][0], numbers[i-1][1])
print(min(numbers[-1]))