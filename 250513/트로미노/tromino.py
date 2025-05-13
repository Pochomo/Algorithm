n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# Please write your code here.
for i in range(n):
    for j in range(m):
        # case 1 계단 모양
        if j + 1 < m and i + 1 < n:
            answer = max(grid[i][j] + grid[i+1][j] + grid[i+1][j+1], answer)
        if j + 1 < m and i - 1 >= 0:
            answer = max(grid[i][j] + grid[i-1][j+1] + grid[i][j+1], answer)
        if j + 1 < m and i + 1 < n:
            answer = max(grid[i][j] + grid[i][j+1] + grid[i+1][j+1], answer)
        if i + 1 < n and j + 1 < m:
            answer = max(grid[i][j] + grid[i+1][j] + grid[i][j+1], answer)

        # case 2 직선
        if j + 2 < m:
            answer = max(grid[i][j] + grid[i][j+1] + grid[i][j+2], answer)
        if i + 2 < n:
            answer = max(grid[i][j] + grid[i+1][j] + grid[i+2][j], answer)

print(answer)