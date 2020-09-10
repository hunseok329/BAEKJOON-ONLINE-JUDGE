num = int(input())

def fibo(n):
    numbers = [[0, 1, 0], [1, 0, 1]]
    if n == 0:
        print(numbers[0][1], numbers[0][2])
    else:
        for i in range(n-1):
            numbers.append(list(map(lambda x, y : x+y, numbers[-1], numbers[-2])))
        print(numbers[-1][-2], numbers[-1][-1])
for _ in range(num):
    fibo(int(input()))