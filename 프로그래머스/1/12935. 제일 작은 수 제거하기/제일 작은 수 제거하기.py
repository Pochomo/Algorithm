def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_num = min(arr)
    result = []
    
    for num in arr:
        if num != min_num:
            result.append(num)
    
    return result