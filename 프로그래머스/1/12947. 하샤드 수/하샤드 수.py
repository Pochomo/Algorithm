def solution(x):
    temp = x
    cnt = 0
    while temp > 0:
        cnt += temp % 10
        temp = temp // 10
    
    if x % cnt == 0:
        return True
    else:
        return False