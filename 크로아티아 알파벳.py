check = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
for i in check:
    count = s.count(i)
    if count == 0:
        continue
    length = len(i)
    for j in range(count):
        a = s.find(i)
        s = s[:a] + 'A' + s[a+length:]
print(len(s))