def solution(a, b, n):
    total = 0
    empty = n
    
    while empty >= a:
        exchange = empty // a
        
        new_cola = exchange * b
        total += new_cola
        
        empty = empty - (exchange * a) + new_cola
    
    return total