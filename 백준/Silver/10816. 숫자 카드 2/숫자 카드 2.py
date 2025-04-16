#10816.py 숫자 카드 2
n = int(input())
arr_n = list(map(int, input().split()))

m = int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()
# 0은 value
count_dict = {key: 0 for key in arr_m}

for num in arr_n:
    if num in count_dict:
        count_dict[num] += 1

for num in arr_m:
    print(count_dict[num], end=' ')