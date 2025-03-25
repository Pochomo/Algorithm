#dp[10] 까지 구성 후 append 하면 쉽다.
n = int(input())
dp = [-1, -1, -1, 1, -1, 1, 2, -1, 2, 3, 2, 3, 4] #12까지
for i in range(13, n+1):
    dp.append(dp[i-5]+1)

print(dp[n])