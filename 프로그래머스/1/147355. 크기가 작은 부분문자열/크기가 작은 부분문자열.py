def solution(t, p):
    answer = 0
    t = list(t)
    for i in range(len(t)-len(p)+1):
        temp = ''.join(t[i:i+len(p)])
        if int(temp) <= int(p):
            answer += 1
                
                
    return answer