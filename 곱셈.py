a,b,c = map(int, input().split())

def mod(x, y, m):
    if y == 0:
        return 1
    if y % 2 == 0:
        temp = mod(x, y//2, m)
        return (temp)**2 % m
    else:
        temp = mod(x, y//2, m)
        return ((temp)**2 % m) * (x % m)%m
print(mod(a, b, c))