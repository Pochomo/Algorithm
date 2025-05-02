def solution(n):
    answer = 0
    base3 = ''
    while (n > 0):
        if n % 3 == 1:
            base3 += '1'
            n //= 3
        elif n % 3 == 2:
            base3 += '2'
            n //= 3
        else:
            base3 += '0'
            n //= 3
    
    cnt = 1
    for i in range(len(base3)-1,-1,-1):
        answer += cnt * int(base3[i])
        cnt *= 3
        
    return answer