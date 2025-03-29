#백준 9251  LCS
n1 = input() #알파벳 대문자 
n2 = input()
dp = [0] * (len(n2) + 1)
for i in range(1, len(n1) + 1):
    temp = 0
    for j in range(1, len(n2) + 1):
        current = dp[j]
        if n1[i-1] == n2[j-1]:
            dp[j] = temp + 1
        else:
            dp[j] = max(dp[j], dp[j-1])
        temp = current
print(max(dp))