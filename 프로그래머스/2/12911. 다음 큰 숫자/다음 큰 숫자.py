def solution(n):
    answer = n
    # n 이진수 변환 후 1의 갯수
    cnt = bin(n)[2:].count("1")
    
    while True:
        answer += 1
        if cnt == bin(answer)[2:].count("1"):
            break
    
    
    return answer