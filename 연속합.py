num = int(input())

numbers = list(map(int, input().split()))

for i in range(1, num):
    temp = numbers[i-1] + numbers[i]
    if numbers[i] < temp:
        numbers[i] = temp
print(max(numbers))