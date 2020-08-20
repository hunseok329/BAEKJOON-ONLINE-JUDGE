n = int(input())
score = list(map(int, input().split()))
total = 0
Max = max(score)
for i in score:
    total += i/Max*100
print(total/n)
