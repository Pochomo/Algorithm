#백준 1463
n = int(input())
dp = [0] * (n+1)

values = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3, 4, 3, 4]

for j in range(min(14, n+1)):
    dp[j] = values[j]

for i in range(14, n+1):
    # 1뺴고 먼저 계산값 초기화
    dp[i] = dp[i-1] + 1
    ## 1빼고랑 나머지 연산을 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[n])