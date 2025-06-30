def solution(food):
    # 1 3 4 6 물, 1번, 2번, 3번
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
            
    answer += '0'
    temp = list(answer)
    temp.reverse()
    temp = ''.join(temp)
    answer += temp[1:]
        
    return answer