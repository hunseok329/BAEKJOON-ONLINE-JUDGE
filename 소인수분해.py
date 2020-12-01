num = int(input())

div = 2
while True:
    if num == 1:
        break
    if num % div == 0:
        num = num // div
        print(div)
    else:
        div += 1