#백준 14567 선수과목 r
n, m = map(int, input().split())
num = []
for _ in range(m):
    w, v = map(int, input().split())
    num.append((w, v))

dp = [1] * (n+1)
num.sort()

for _ in range(n):
    for a, b in num:
        #b 듣기 위해서는 a 들은 다음 학기여야 함
        if dp[b] <= dp[a]:
            dp[b] = dp[a] + 1

print(*dp[1:])

