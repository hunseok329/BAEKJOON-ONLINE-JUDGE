num = int(input())
result = 0
for i in range(num):
    string = input()
    check = []
    for word in string:
        if word not in check:
            check.append(word)
        elif word == check[-1]:
            check.append(word)
        else:
            break
    else:
        result += 1
print(result)