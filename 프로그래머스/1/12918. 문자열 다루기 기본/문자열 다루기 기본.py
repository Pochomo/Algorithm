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

#def alpha_string46(s):
#   import re
#    return bool(re.match("^(\d{4}|\d{6})$", s))

# s.isdigit()을 써도된다.