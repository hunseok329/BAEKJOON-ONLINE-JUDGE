mul = 1
for _ in range(3):
    n = int(input())
    mul *= n
mul = str(mul)
for i in range(10):
    num = mul.count(str(i))
    print(num)
