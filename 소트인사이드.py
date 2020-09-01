number = str(input())
result = []
for i in number:
    result.append(i)
result = sorted(result,key = lambda x: int(x), reverse = True )
print("".join(result))
