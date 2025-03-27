#5557.py 1학년
n = int(input())
num = list(map(int, input().split()))
 
goal = num[-1] #도달해야하는 숫자

dp = [[0] * 21 for _ in range(n-1)] #dp[i][j] i번째까지 계산했을때 값 j

dp[0][num[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j] > 0:
            if j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i-1][j]
            if j - num[i] >= 0:
                dp[i][j - num[i]] += dp[i-1][j]

print(dp[-1][goal])