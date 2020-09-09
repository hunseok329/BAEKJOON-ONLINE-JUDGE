num = int(input())

for i in range(num):
    string = str(i)
    number = 0
    for n in string:
        number += int(n)
    if i+number == num:
        print(i)
        break
else:
    print(0)