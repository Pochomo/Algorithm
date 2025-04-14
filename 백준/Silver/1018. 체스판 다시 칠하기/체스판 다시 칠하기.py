n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input())
    
# 이 보드를 잘라서 8×8 크기의 체스판
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
result = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        count_w = 0
        count_b = 0
        
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r + c) % 2 == 0:
                    # 시작이 흰색일 경우 짝수 칸은 흰색
                    if arr[r][c] != 'W':
                        count_w += 1
                    # 시작이 검은색일 경우 짝수 칸은 검은색
                    if arr[r][c] != 'B':
                        count_b += 1
                else:
                    # 시작이 흰색일 경우 홀수 칸은 검은색
                    if arr[r][c] != 'B':
                        count_w += 1
                    # 시작이 검은색일 경우 홀수 칸은 흰색
                    if arr[r][c] != 'W':
                        count_b += 1
        
        result = min(result, count_w, count_b)

print(result)