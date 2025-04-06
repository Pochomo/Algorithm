#2141 우체국

n = int(input())
villiage = []

total_people = 0
for _ in range(n):
    house, people = map(int, input().split())
    total_people += people
    villiage.append((house, people))

villiage.sort(key= lambda x: x[0])

#중앙값을 찾는것에 초점을 맞추다.
cnt = 0
for i in range(n):
    cnt += villiage[i][1]
    if cnt >= total_people/2:
        print(villiage[i][0])
        break