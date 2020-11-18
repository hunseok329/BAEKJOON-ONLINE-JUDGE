num = int(input())

numbers = []
checkList = []
result = []
s = []
index = 0

for _ in range(num):
    numbers.append(int(input()))

for i in range(1, num+1):
    while len(s) != 0:
        if numbers[index] == s[-1]:
            checkList.append(s.pop())
            index += 1
            result.append("-")
        else:
            break
    s.append(i)
    result.append("+")

while len(s) != 0:
    checkList.append(s.pop())
    result.append("-")
        
if checkList != numbers:
    print("NO")
else:
    for p in result:
        print(p)