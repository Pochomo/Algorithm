#11000 강의실 배정 힙을 사용해야됨, pop사용했을 때 시간초과발생
import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = []

for _ in range(n):
    start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

rooms = []

heapq.heappush(rooms, lectures[0][1])

for i in range(1, n):
    start, end = lectures[i]
    if start >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)

print(len(rooms))