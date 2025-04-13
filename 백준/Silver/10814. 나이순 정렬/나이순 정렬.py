# 10814 백준 나이순 정렬
# 회원을 나이 순, 나이가 같으면 가입한 순
n = int(input())
arr = []
for i in range(n):
    x, y = (input().split())
    arr.append((x, y))

arr.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(*arr[i])