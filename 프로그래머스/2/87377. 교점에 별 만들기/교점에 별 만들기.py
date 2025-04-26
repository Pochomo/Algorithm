def solution(line):
    pos, answer = [], []
    n = len(line)
    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c: continue # 두 직선이 평행한 경우
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

    height = (y_max - y_min + 1)
    width = (x_max - x_min + 1)
    
    arr = [['.'] * width for _ in range(height)]
    
    for x, y in pos:
        row = y_max - y
        col = x - x_min
        arr[row][col] = '*'
    
    answer = [''.join(row) for row in arr]
    
    # 시간 초과 발생 매번 새로운 문자열을 만드는 것은 비효율적이다
    #for x, y in pos:
    #    row = y_max - y
    #    col = x - x_min
    #    answer[row] = answer[row][:col] + '*' + answer[row][col+1:]
    
    return answer