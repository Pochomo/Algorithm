def solution(s):
    answer = list(s)
    if len(answer) % 2 == 1:
        temp = len(answer) // 2
        ans = answer[temp]
    else:
        temp = len(s) // 2 - 1
        ans = answer[temp:temp+2]
    
    ans = ''.join(ans)
    return ans