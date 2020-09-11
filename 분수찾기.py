num = int(input())
result = [0,0]
for i in range(1, 10000000):
    if i < num:
        num -= i
        continue
    if i % 2 == 0:
        result[1] = i-num+1
        result[0] = (i+1)-result[1]
    else:
        result[0] = i-num+1
        result[1] = (i+1)-result[0]
    break
print(str(result[0]) + '/' + str(result[1]))