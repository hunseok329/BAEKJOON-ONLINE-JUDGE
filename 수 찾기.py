N = int(input())

check = list(map(int, input().split()))
check = sorted(check)

M = int(input())

numbers = list(map(int, input().split()))

def search(n, front, end):
    global check
    half = (end + front) // 2
    
    if front > end:
        return False
    if n == check[half]:
        return True
    elif n > check[half]:
        return search(n, half+1, end)
    else:
        return search(n, front, half-1)
    
for num in numbers:
    if search(num, 0, N-1):
        print(1)
    else:
        print(0)