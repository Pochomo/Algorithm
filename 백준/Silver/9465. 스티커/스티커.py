#백준 9465
def cal_dp(n):
    if n == 1:
        return max(arr[0][0], arr[1][0])

    dp = [[0] * n for _ in range(2)]

    #아래 부터 시작, 위부터 시작 나눠서 계산산
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for i in range(1, n):
        if i == 1:
            dp[0][i] = arr[0][i] + dp[1][0]
            dp[1][i] = arr[1][i] + dp[0][0]
        else:
            dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])
    return max(dp[0][n-1], dp[1][n-1])

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    print(cal_dp(n))
