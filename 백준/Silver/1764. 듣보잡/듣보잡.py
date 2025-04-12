#1764 듣보잡
n, m = map(int, input().split())

d = set()
for _ in range(n):
    d.add(input())

result = []
for _ in range(m):
    name = input()
    if name in d:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)