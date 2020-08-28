num = input()
p = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
count = 0
for i in num:
    if i in p[0]:
        count += 3
    if i in p[1]:
        count += 4
    if i in p[2]:
        count += 5
    if i in p[3]:
        count += 6
    if i in p[4]:
        count += 7
    if i in p[5]:
        count += 8
    if i in p[6]:
        count += 9
    if i in p[7]:
        count += 10
print(count)