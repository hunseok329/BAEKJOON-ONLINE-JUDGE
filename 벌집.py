num = int(input())
if num == 1:
    print(1)
else:
    n = 1 
    num -= 1
    while num > n*6:
        num -= n*6
        n += 1
    print(n+1)