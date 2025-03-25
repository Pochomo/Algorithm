import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#도착지점까지 가는 경우의 수는 도착지점이 아닌 임의의 점들에서 도착지점까지 가는 경우의 수와 똑같다.
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    #이미 방문했으면 그 위치에서 출발하는 경우의 수 리턴 , 그 자리에서 도달은 결국 가능 함으로로
    if dp[x][y] != -1:
        return dp[x][y] 
    
    chance = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx and nx < m and 0 <= ny and ny < n and graph[nx][ny] < graph[x][y] : #0 <= nx < m 도 가능
            chance += dfs(nx, ny)
            
    dp[x][y] = chance
    return dp[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))