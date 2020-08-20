n = int(input())
for _ in range(n):
    string = list(map(int, input().split()))
    score = sum(string[1:])
    standard = score//string[0]
    count = 0
    for i in string[1:]:
        if i > standard:
            count += 1
    result = (count/string[0])*100
    print("{0:.3f}%".format(result))
