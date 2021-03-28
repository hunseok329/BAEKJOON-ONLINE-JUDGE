n, k = map(int, input().split())

num = [i for i in range(1, n+1)]

result = []

pn = 0
while num:
    pn += k-1
    if pn < len(num):
        result.append(num.pop(pn))
    else:
        pn = pn % len(num)
        result.append(num.pop(pn))
        
ans = "<"

for x in result:
    ans += str(x) + ", "
print(ans[:-2] + ">")