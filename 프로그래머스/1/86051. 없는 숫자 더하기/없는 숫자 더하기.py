
def solution(numbers):
    result = 0
    
    for i in range(10):
        found = False
        for j in range(len(numbers)):
            if numbers[j] == i:
                found = True
                break
        if not found:
            result += i
    
    return result