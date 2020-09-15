num = int(input())

count = 0
check = True
while num > 0:
    if num%5 == 0:
        print(num//5 + count)
        check = False
        break
    else:
        num -= 3
        count += 1
if check:
    if num==0:
        print(count)
    else:
        print(-1)