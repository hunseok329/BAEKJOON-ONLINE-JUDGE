num = int(input())
count = 0
if num < 100:
    print(num)
else:
    for i in range(100, num+1):
        string = str(i)
        c = 10
        for j in range(len(string)-1):
            n = int(string[j]) - int(string[j+1])
            if c == 10:
                c = n
            else:
                if n != c:
                    break
        else:
            count += 1
    print(count + 99)
                    