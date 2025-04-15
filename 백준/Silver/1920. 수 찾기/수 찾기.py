#1920 수 찾기

n = int(input())

arr = list(map(int, input().split()))

arr = set(arr)

m = int(input())

arr_m = list(map(int, input().split()))

for i in range(m):
    if arr_m[i] in arr:
        print('1')
    else:
        print('0')