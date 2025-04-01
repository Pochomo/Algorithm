#백준 1548
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 2 if n >= 2 else 1 

for i in range(n-2):
    for j in range(i+1, n-1):
        end = j + 1
        while True:
            if arr[i] + arr[j] > arr[end]:
                answer = max(answer, end - j + 2)
                end += 1
                if end==n:break
            else:
                break
print(answer)
