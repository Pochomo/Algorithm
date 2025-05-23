import sys
input = sys.stdin.readline

n = int(input())

stars = [[' ']*2*n for _ in range(n)]

def make_star(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    
    else:
        newSize = size//2
        make_star(i, j, newSize)
        make_star(i + newSize, j - newSize, newSize)
        make_star(i + newSize, j + newSize, newSize)

make_star(0, n - 1, n)
for star in stars:
    print("".join(star))