num = int(input())

numbers = list(map(int, input().split()))
numbers.sort()
half = num//2
if num % 2 == 0:
    print(numbers[half-1]*numbers[half])
else:
    print(numbers[half]*numbers[half])