#20207 달력 
n = int(input())

calendar = [[0] * 366 for _ in range(n)]

arr = list()

for _ in range(n):
    s, e = map(int, input().split())
    term = e - s + 1
    arr.append((s, e, term))

arr.sort(key = lambda x: (x[0]))

for i in range(len(arr)):
    s, e = arr[i][0],arr[i][1]
    for j in range(n):
        if 1 in calendar[j][s:e + 1]:
            continue

        for k in range(s, e + 1):
            calendar[j][k] = 1
        break

ans = 0
row = 0
col = 0
for i in range(1, 366):
    check = False
    for j in range(n):
        if calendar[j][i] == 1:
            check = True
            row = max(row, j + 1)
    if check:
        col += 1
    else:
        ans += col * row
        row = 0
        col = 0
if check:
    ans += col * row
print(ans)
