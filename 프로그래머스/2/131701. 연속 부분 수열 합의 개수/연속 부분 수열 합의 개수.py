def solution(elements):
    total = sum(elements)
    answer = []
    
    # 원형 배열을 위해
    extend = elements + elements
    
    for cnt in range(1, len(elements) + 1):
        for start in range(len(elements)):
            answer.append(sum(extend[start:start+cnt]))
    
    answer = set(answer)
    return len(answer)