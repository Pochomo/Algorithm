def solution(n, m, section):
    painted = 0
    answer = 0
    for i in section:
        if i > painted:
            painted = i + m -1
            answer += 1
    
    return answer