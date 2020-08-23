word = input().upper()
check = list(set(word))
result = []
for i in check:
    result.append(word.count(i))
Max = max(result)
if result.count(Max) != 1:
    print("?")
else:
    index = result.index(Max)
    print(check[index])
