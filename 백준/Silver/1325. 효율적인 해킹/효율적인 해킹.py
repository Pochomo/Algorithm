import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)  #리스트로 방문 처리 set 사용시 시간초과 발생생
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_count = 0

for i in range(1, N + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)


# import sys
# input = sys.stdin.readline

# def dfs(start, graph):
#     stack = [start]
#     visit = set([start]) #set([start])를 하면서 반복처리를 안 할 수 있도록 함 밑에서 visit를 반복문 if 안에 삽입
#     count = 1

#     while stack:
#         node = stack.pop()
#         for neighbor in graph[node]:
#             if neighbor not in visit:
#                 visit.add(neighbor)
#                 stack.append(neighbor)
#                 count += 1
#     return count

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)] #O(N+M) 위해서서

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[b].append(a)

# result = []
# max_count = 0

# for i in range(1, N + 1):
#     count = dfs(i, graph)
#     if count > max_count:
#         max_count = count
#         result = [i]
#     elif count == max_count:
#         result.append(i)

# print(*result)
