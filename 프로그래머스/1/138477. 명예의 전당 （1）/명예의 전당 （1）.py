def solution(k, score):
    answer = []
    hof = []
    for s in score:
        if len(hof) < k:
            hof.append(s)
        else:
            if s > min(hof):
                hof.remove(min(hof))
                hof.append(s)
        answer.append(min(hof))
    return answer
