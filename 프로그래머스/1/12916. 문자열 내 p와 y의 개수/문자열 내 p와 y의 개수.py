def solution(s):
    answer = True
    cntP = 0
    cntY = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            cntP += 1
        if s[i] == 'y' or s[i] == 'Y':
            cntY += 1
    if cntP == cntY:
        return True
    else: return False