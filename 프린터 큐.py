num = int(input())


for _ in range(num):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    i = 0
    count  = 1
    while True:
        maximum = max(numbers)
        if i == N:
            i = 0

        if maximum == numbers[M] and M == i:
            print(count)
            break

        if numbers[i] == maximum:
            numbers[i] = -1
            count += 1
        i += 1   