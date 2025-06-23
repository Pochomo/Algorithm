def solution(n, m):
    answer = []
    smaller = min(n, m)
    bigger = max(n, m)
    while True:
        if n % smaller == 0 and m % smaller == 0:
            answer.append(smaller)
            break
        smaller -= 1
            
    while True:
        if bigger % n == 0 and bigger % m == 0:
            answer.append(bigger)
            break
        bigger += 1
    
    return answer