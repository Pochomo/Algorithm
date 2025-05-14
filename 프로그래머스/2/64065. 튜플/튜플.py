import re

def solution(s):
    # 중복이 있을 수 있고, 순서가 다르면 다른 튜플
    # 원소 개수는 유한
    answer = []
    matches = re.findall(r"\{([\d,]+)\}", s)
    result = [list(map(int, group.split(','))) for group in matches]
    result.sort(key = lambda x : len(x))
    
    for elm in result:
        for i in range(len(elm)):
            if elm[i] not in answer:
                answer.append(elm[i])

    return answer