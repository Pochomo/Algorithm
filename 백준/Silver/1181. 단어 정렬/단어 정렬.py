#1181 단어 정렬
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

#중복을 제거하고 정렬해야됨
arr = list(set(arr)) #중복제거

arr.sort(key = lambda x: (len(x), x))

for i in arr:
    print(i)