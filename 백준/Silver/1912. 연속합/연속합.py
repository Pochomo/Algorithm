#1912
def cal(n, a_input):
    dp = [0] * (n+1)
    dp[0] = a_input[0]
    max_num = a_input[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + a_input[i], a_input[i])
        max_num = max(max_num, dp[i])
    return max_num

n = int(input())
a_input = list(map(int, input().split()))
result = cal(n, a_input)
print(result)
                                                                                                                                                                                                                             