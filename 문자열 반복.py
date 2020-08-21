n = int(input())
for _ in range(n):
    num, string = map(str, input().split())
    result = ""
    for i in string:
        result += i*int(num)
    print(result)
