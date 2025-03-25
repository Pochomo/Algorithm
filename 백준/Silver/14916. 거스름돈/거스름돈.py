
def cal_min_coin(n):
    dp = [[0,0] for _ in range(100001)]
    #dp[2의 갯수, 5의 갯수]

    dp[5] = [0, 1] #홀수 첫 수 5는 0, 1로 시작

    if n % 2 == 1: #홀수
        for i in range(1, n + 1, 2):
            if i > 5:
                if dp[i-2][0] == 4:
                    dp[i] = [dp[i-2][0] - 4, dp[i-2][1] + 2]
                else: dp[i] = [dp[i-2][0] + 1, dp[i-2][1]]

    elif n % 2 == 0: #짝수
        for i in range(0, n + 1, 2):
            if i >= 2:
                if dp[i-2][0] == 4:
                    dp[i] = [dp[i-2][0] - 4, dp[i-2][1] + 2]
                else: dp[i] = [dp[i-2][0] + 1, dp[i-2][1]]

    return dp[n][0] + dp[n][1]


n = int(input())

if cal_min_coin(n) == 0:
    print(-1)
else:
    print(cal_min_coin(n))