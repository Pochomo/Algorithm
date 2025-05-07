import re
def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6):
        if re.search(r'[a-zA-Z]', s):
            answer = False
        else:
            answer = True
    else:
        answer = False   
    return answer