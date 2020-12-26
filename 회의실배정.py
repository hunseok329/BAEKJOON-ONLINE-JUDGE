import sys

num = int(sys.stdin.readline())

arr = []
for _ in range(num):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr = sorted(arr, key=lambda x : (x[1], x[0]))


meeting_room = 0
start_time = 0

for time in arr:
    if time[0] >= start_time:
        start_time = time[1]
        meeting_room += 1
print(meeting_room)