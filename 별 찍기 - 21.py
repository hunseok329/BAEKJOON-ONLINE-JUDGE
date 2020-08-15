n = int(input())
if n == 1:
    print('*')
else:
    num = n // 2
    s = ''
    if n % 2 == 0:
        s = ' *'*num
        for _ in range(n):
            print(s[1:])
            print(s)
    else:
        s = ' *'*(num+1)
        for _ in range(n):
            print(s[1:])
            print(s[:-2])
