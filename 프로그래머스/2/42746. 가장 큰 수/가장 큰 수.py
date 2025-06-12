def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x: x*10, reverse=True)

    answer = ''.join(num)
    
    if answer[0] == '0':
        return '0'
    
    return answer