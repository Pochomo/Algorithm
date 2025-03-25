def cal(n, dp):
    if n < len(dp):
        return dp[n]
    
    for i in range(len(dp), n + 1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[n]

n = int(input())
dp = [0, 1, 2, 4]

for i in range(n):
    print(cal(int(input()), dp))
