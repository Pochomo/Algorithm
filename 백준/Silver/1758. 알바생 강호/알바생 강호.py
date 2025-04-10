#1758.py
from collections import deque

n = int(input())

people_list = []
for _ in range(n):
    people_list.append(int(input()))

people_list.sort(reverse=True)

people = deque(people_list)

money = 0
index = 1
while len(people) > 0:
    cnt = people.popleft()
    tip = cnt - (index - 1)
    if tip > 0:
        money += tip
    index += 1

print(money)