from collections import Counter
import sys
num = int(sys.stdin.readline())

numbers = []
s = 0
for _ in range(num):
    n = int(sys.stdin.readline())
    numbers.append(n)
    s += n

numbers.sort()

print('%.f' %(s/num))
print(numbers[num//2])

if num != 1:
    cnt = Counter(numbers).most_common()
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(numbers[0])
print(numbers[-1]-numbers[0])