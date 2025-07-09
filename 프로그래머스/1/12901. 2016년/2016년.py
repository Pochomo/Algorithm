def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total = sum(month[:a - 1]) + b
    
    answer = day[total % 7]
    
    return answer
