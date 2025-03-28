#백준 2294.py 동전 2
n, k = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))

dp = [float("inf")] * (k+1)
dp[0] = 0

for coin in num:
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[k] == float("inf"):
    print(-1)
else:
    print(dp[k])
