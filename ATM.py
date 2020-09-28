num = int(input())

numbers = list(map(int, input().split()))
result = 0
temp = 0
numbers.sort()

for i in numbers:
    temp += i
    result += temp
print(result)
