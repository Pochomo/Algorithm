#2217 백준 로프
n = int(input())

rope = []
# 로프의 최대 중량
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
# n 개 고르면 그 n개의 /k 배 만큼 들 수 있음
result = rope[0]
for i in range(1, n):
    result = max(result, rope[i] * (i + 1))


print(result)