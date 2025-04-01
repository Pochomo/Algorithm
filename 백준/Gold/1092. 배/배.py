#1092
import sys
input = sys.stdin.readline

n = int(input()) #무게 제한 수
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0

if cranes[0] < boxes[0]:
    cnt = -1
else:
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        cnt += 1

print(cnt)