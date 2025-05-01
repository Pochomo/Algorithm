def solution(num, cnt=0):
    if cnt >= 500:
        return -1
    if num == 1:
        return cnt
    if num % 2 == 0:
        return solution(num // 2, cnt + 1)
    else:
        return solution(num * 3 + 1, cnt + 1)