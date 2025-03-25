def cal_dp(n):
    if n == 1:
        return a_input[0]
    if n == 2:
        return a_input[0] + a_input[1]
    
    dp = [0] * n
    dp[0] = a_input[0]
    dp[1] = a_input[0] + a_input[1]
    #세 번째 잔까지 고려
    dp[2] = max(a_input[0] + a_input[2], a_input[1] + a_input[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + a_input[i], dp[i-3] + a_input[i-1] + a_input[i])

    return dp[n-1]

a_input = []
n = int(input())
for i in range(n):
    a_input.append(int(input()))

print(cal_dp(n))