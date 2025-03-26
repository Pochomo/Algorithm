#백준21337 징검다리 건너기

def cal_dp(n, k, graph):
    dp = [[0, 0] for _ in range(n)]
    
    dp[0][1] = 50000
    
    for i in range(1, n):
        if i == 1:
            dp[i][0] = graph[0][0]
        elif i == 2:
            dp[i][0] = min(dp[i-1][0] + graph[i-1][0], dp[i-2][0] + graph[i-2][1])
        else:
            dp[i][0] = min(dp[i-1][0] + graph[i-1][0], dp[i-2][0] + graph[i-2][1])

        dp[i][1] = 50000
        
        if i >= 3:
            dp[i][1] = min(dp[i][1], dp[i-3][0] + k)
        
        if i >= 1:
            dp[i][1] = min(dp[i][1], dp[i-1][1] + graph[i-1][0])
        if i >= 2:
            dp[i][1] = min(dp[i][1], dp[i-2][1] + graph[i-2][1])
    
    return min(dp[n-1][0], dp[n-1][1])

n = int(input())
graph = []
for _ in range(n-1):
    s, b = map(int, input().split())
    graph.append([s, b])
k = int(input())

print(cal_dp(n,k,graph))