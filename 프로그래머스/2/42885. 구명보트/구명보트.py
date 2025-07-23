from collections import deque
# 데크 사용해서 맨 앞 뺄 때 o(1) 로
def solution(people, limit):
    cnt = 0
    people = deque(sorted(people))

    while people:
        person = people.pop()
    
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()
            
        cnt += 1
    
    return cnt