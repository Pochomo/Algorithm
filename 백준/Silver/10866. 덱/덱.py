#10866 백준 덱덱
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

de_queue = deque()

for _ in range(n):
    command = input().split()
    if command[0] == 'push_back':
        de_queue.append(command[1])

    elif command[0] == 'push_front':
        de_queue.appendleft(command[1])

    elif command[0] == 'pop_front':
        if len(de_queue) == 0:
            print(-1)
        else:
            temp = de_queue.popleft()
            print(temp)

    elif command[0] == 'pop_back':
        if len(de_queue) == 0:
            print(-1)
        else:
            temp = de_queue.pop()
            print(temp)

    elif command[0] == 'size':
        print(len(de_queue))
    elif command[0] == 'empty':
        if len(de_queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(de_queue) == 0:
            print(-1)
        else:
            print(de_queue[0])
    elif command[0] == 'back':
        if len(de_queue) == 0:
            print(-1)
        else:
            print(de_queue[-1])
    