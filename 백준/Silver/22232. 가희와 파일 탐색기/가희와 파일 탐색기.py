#백준 22322 파일 확장자
def custom(file):
    if '.' in file:
        filename, extension = file.rsplit('.', 1)
    else:
        filename, extension = file, ""
    
    is_supported = extension in os_set
    return (filename, not is_supported, extension)

n, m = map(int, input().split())
file_list = []
for _ in range(n):
    file_list.append(input())
os_set = set(input() for _ in range(m))

file_list.sort(key=custom)

for file in file_list:
    print(file)

# 리스트 탐색을 하면 O(m)이기 떄문에 set 을 써서 O(1)로 해야한다 중요.

