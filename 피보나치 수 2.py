num = int(input())

numbers = [0, 1]

for i in range(num-1):
    numbers.append(numbers[-1] + numbers[-2])
print(numbers[-1])
