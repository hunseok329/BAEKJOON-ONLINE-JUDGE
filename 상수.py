numbers = list(map(str, input().split()))
for i in range(len(numbers)):
    numbers[i] = int(numbers[i][::-1])
print(max(numbers))
