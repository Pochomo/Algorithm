def solution(x, n):
    answer = []
    cnt = 0
    start = x
    while cnt < n:
        answer.append(start)
        start += x
        cnt += 1
    return answer