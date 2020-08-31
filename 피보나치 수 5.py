num = int(input())
def febo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return febo(n-1) + febo(n-2)
print(febo(num))