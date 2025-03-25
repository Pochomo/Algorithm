#백준 10844 R 
def cal_dp(n):
    dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n)]
    for i in range(1, 10):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif 1 <= j <= 8:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            else:
                dp[i][j] = dp[i-1][j-1]

    max = 0
    for i in range(10):
        max += dp[n-1][i]

    return max 
    
n = int(input())
print(cal_dp(n) % 1000000000) 