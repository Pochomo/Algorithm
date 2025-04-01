#1931.py
import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))
    #meeting.append([map(int, input().split())]) (X) 리스트에 map 객체들어감

meeting.sort(key=lambda x: (x[1], x[0])) #x[1] 부터 정렬, 그 후 같으면 x[0] 정렬

cnt = 0
end_time = 0

for start, end in meeting:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)