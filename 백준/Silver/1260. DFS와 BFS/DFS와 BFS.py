from collections import deque #popleft()는 O(1)이기 때문에 deque 사용 pop(0)이 O(n) 이라 queue 라이브러리 사용 안함

def dfs(graph, start): #스택사용
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node) #방문 표시
            for neighbor in range(len(graph[node]) - 1, -1, -1):  
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

def bfs(graph, start): #큐 사용
    queue = deque([start])  #BFS는 큐 사용
    visited = set()  #방문한 노드 저장

    while queue:
        node = queue.popleft()  #큐에서 꺼내기
        if node not in visited:
            print(node, end=" ")  #탐색된 순서
            visited.add(node)  #방문 표시
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)
                    
n, m, start = map(int, input().split())
graph = []
for _ in range(n + 1):
    graph.append([0] * (n + 1))

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

dfs(graph, start)
print()
bfs(graph, start)