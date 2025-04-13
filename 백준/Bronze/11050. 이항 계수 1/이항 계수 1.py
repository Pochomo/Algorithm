#11050.py 이항 계수
n, k = map(int, input().split())

top = 1
for i in range(n, 0, -1):
    top *= i

bottom = 1
for j in range(n-k, 0, -1):
    bottom *= j

for j in range(k, 0, -1):
    bottom *= j

print(top // bottom)