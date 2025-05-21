def solution(n):
    answer = 0
    cnt = 1
    while cnt ** 2 <= n:
        if cnt ** 2 == n:
            cnt += 1
            answer = cnt ** 2
            return answer
            break
        else:    
            cnt += 1
        answer = -1
    return answer