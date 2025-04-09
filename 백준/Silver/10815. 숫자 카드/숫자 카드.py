n = int(input())
arr = set(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

result = []
for check in check_list:
    if check in arr:
        result.append(1)
    else:
        result.append(0)

print(*result)