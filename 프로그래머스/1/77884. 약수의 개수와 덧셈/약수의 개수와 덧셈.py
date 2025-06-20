def solution(left, right):
    answer = 0
    # 약수 짝수면 더하고 홀수면 뺌
    for num in range(left, right+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer