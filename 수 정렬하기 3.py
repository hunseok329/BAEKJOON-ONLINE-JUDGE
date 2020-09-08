import sys

num = int(sys.stdin.readline())
numbers = [0]*10001
check = []
for _ in range(num):
    n = int(sys.stdin.readline())
    numbers[n] += 1
for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)