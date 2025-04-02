#13164 행복 유치원
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tall = list(map(int, input().split()))

tall.sort()

diff = []

for i in range(1, n):
    diff.append(tall[i] - tall[i-1])

diff.sort(reverse=True)


print(sum(diff[m-1:]))
