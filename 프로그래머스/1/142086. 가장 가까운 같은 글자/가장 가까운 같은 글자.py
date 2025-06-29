def solution(s):
    answer = []
    checked = {}

    for i in range(len(s)):
        c = s[i]
        if c in checked:
            answer.append(i - checked[c])
        else:
            answer.append(-1)
        checked[c] = i
        
    return answer
