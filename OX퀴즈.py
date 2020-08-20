n = int(input())

for _ in range(n):
    string = input()
    result = 0
    count = 0
    for word in string:
        if word == "O":
            count += 1
            result += count
        else:
            count = 0
    print(result)
