num = int(input())

arr = list(map(int, input().split()))

def div(a, b):
    n = a
    m = b
    c = 2
    while True:
        if n % c == 0 and m % c == 0:
            n = n//c
            m = m//c
        else:
            c += 1
        if c > n or c > m:
            break
    return [n, m]

for i in range(1, num):
    temp = div(arr[0], arr[i])
    print(str(temp[0]) + '/' + str(temp[1]))