def solution(k, m, score):
    score.sort(reverse=True)
    
    total = 0
    
    for i in range(0, len(score) - m + 1, m):
        box = score[i:i + m]
        total += min(box) * m
    
    return total
