n = int(input())
t = []
p = []

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0] * (n + 1)

for i in range(n):
    if i + 1 <= n:
        dp[i + 1] = max(dp[i + 1], dp[i])
    
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

print(dp[n])
