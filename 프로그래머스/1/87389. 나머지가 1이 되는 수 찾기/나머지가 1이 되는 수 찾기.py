def solution(n):
    answer = 1000000
    for i in range(1, n):
        if n % i == 1:
            answer = min(i, answer)
    return answer