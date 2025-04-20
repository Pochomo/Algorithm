# 10994 별 찍기
def star(n, x, y):
    
    length = (4*n)-3
    if length == 1:
        array[x][y] = "*"
        return
    
    else:
        for i in range(length):
            array[x][y+i] = "*"
            array[y+i][x] = "*"
            array[x+(length-1)][y+i] = "*"
            array[x+i][y+(length-1)] = "*"
        n = n-1
        x = x+2
        y = y+2
        star(n, x, y)
        return

n = int(input())
length = (4*n)-3
array = [[' ']*(length) for _ in range(length)]

star(n, 0, 0)
for i in range(length):
    print(*array[i], sep = '')
