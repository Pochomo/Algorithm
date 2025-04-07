#백준 좌표 정렬하기 11650
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    xi, yi = map(int, input().split())
    arr.append((xi, yi))
 
arr.sort(key = lambda x : (x[0] , x[1]))

for i in range(n):
    print(*arr[i])