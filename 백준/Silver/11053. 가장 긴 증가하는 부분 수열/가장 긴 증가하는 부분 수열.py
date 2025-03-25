#백준 11053
def cal(n, a_input):
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if a_input[i] > a_input[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

n = int(input())
a_input = list(map(int, input().split()))
result = cal(n, a_input)
print(result)