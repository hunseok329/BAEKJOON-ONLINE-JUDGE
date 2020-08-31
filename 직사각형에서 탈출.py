x,y,w,h = map(int, input().split())
result = []
if abs(x-w) > x:
    result.append(x)
else:
    result.append(abs(x-w))
if abs(y-h) > y:
    result.append(y)
else:
    result.append(abs(y-h))
print(min(result))