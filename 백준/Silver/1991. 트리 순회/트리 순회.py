def preorder_traversal(node, graph, result):
    if node == '.':
        return
    
    result.append(node)
    preorder_traversal(graph[node][0], graph, result)
    preorder_traversal(graph[node][1], graph, result)

    return result

def inorder_traversal(node, graph, result):
    if node == '.':
        return
    
    if node in graph:
        inorder_traversal(graph[node][0], graph, result)
        result.append(node)
        inorder_traversal(graph[node][1], graph, result)
    
    return result

def postorder_traversal(node, graph, result):
    if node == '.':
        return
    
    if node in graph:
        postorder_traversal(graph[node][0], graph, result)
        postorder_traversal(graph[node][1], graph, result)
    result.append(node)
    
    return result

n = int(input())
graph = {}

for _ in range(n):
    root, l, r = input().split()
    graph[root] = [l, r]


print(''.join(preorder_traversal('A', graph, [])))
print(''.join(inorder_traversal('A', graph, [])))
print(''.join(postorder_traversal('A', graph, [])))