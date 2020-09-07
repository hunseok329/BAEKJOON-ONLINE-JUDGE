a,b,c = map(int , input().split())

if b < c:
    num = a//(c-b)
    print(num+1)
else:
    print(-1)