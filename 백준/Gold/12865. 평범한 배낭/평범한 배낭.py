# 백준 12865 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = []
for _ in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

dp= [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n + 1):
    weight, value = item[i-1]
    for j in range(k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)


print(dp[n][k])
