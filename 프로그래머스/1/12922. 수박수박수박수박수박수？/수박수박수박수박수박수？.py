def solution(n):
    answer = ''
    str1, str2 = '수', '박'
    cnt = 0
    while cnt < n:
        cnt += 1
        if cnt % 2 == 0:
            answer = answer + str2
        elif cnt % 2 == 1:
            answer = answer + str1
    return answer