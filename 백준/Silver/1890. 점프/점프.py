import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

def dfs(x, y):
    if x == n-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y] 
    
    if graph[x][y] == 0:
        return 0
    
    chance = 0
    for i in range(2):
        nx, ny = x + dx[i] * graph[x][y] , y + dy[i] * graph[x][y]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            chance += dfs(nx, ny)
            
    dp[x][y] = chance
    return dp[x][y]
    

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

print(dfs(0,0))
