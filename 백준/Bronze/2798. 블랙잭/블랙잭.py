#백준 2798 카지노
#카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
#M을 넘지 않으면서 M과 최대한 가깝게
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] <= m:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)