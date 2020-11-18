a, b = map(int, input().split())

def gcd(n, m):
    while m > 0:
        r = m
        m = n % m
        n = r
    return n

print(gcd(a, b))
print((a*b)//gcd(a, b))