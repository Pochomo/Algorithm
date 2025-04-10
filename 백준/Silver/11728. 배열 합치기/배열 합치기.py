#11728.py
n, m = map(int, input().split())

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

list_1.extend(list_2)

list_1.sort()

print(*list_1)