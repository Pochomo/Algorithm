# 120도 회전 반시계, 시계, 대칭

# 회전
def rotation(tri):
    temp = []
    for i in range(1, n+1):
        temp.append([0 for i in range(i)])
    for i in range(n):
        for j in range(i,n):
            temp[n-i-1][j-i] = tri[j][i]
    return temp

# 대칭
def symmetry(tri):
    temp = []
    for i in range(1, n+1):
        temp.append([0 for _ in range(i)])
    for i in range(n):
        for j in range(len(tri[i])):
            temp[i][len(tri[i]) - 1 - j] = tri[i][j]
    return temp

# 차 찾기
def cal(tri1, tri2):
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if tri1[j][i] != tri2[j][i]:
                cnt += 1
    return cnt


n = int(input())
tri1 = []
tri2 = []

result = float('inf')

for i in range(n):
    m = list(map(int, input().split()))
    tri1.append(m)

for i in range(n):
    m = list(map(int, input().split()))
    tri2.append(m)

# 3번 회전에 가장 작은 차이 찾기
for i in range(3):
    result = min(result, cal(tri1, tri2))
    tri1 = rotation(tri1)

# 대칭 후 대칭한거 회전하면서 비교
sym = symmetry(tri1)

for i in range(3):
    result = min(result,cal(sym, tri2))
    sym = rotation(sym)

print(result)