#백준 11055
def cal(n, a_input):
    dp = [0] * n 
    for i in range(0, n): #각자 자기 자신이 최대 값으로 시작
        dp[i] = a_input[i]

    max_num = 0
    for i in range(1, n):
        for j in range(i):
            if a_input[i] > a_input[j]:
                dp[i] = max(dp[i], dp[j] + a_input[i])
    
    return max(dp)

n = int(input())
a_input = list(map(int, input().split()))
result = cal(n, a_input)
print(result)