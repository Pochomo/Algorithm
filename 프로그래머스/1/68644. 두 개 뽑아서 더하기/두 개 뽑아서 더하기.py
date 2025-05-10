def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers), 1):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))

    answer.sort()
    
    return answer