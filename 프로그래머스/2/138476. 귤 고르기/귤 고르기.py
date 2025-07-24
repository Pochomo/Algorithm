def solution(k, tangerine):
    time = {}
    
    for size in tangerine:
        if size in time:
            time[size] += 1
        else:
            time[size] = 1
        
    cnt = list(time.values())
    cnt.sort(reverse = True)
    
    # 큰 수 부터
    answer = 0
    total = 0
    for i in cnt:
        total += i
        answer += 1
        if total >= k:
            break
    
    return answer