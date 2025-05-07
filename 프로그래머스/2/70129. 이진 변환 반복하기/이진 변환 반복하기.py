def solution(s):
    result = []
    base2 = []
    total, cnt = 0, 0
    base2 = list(s)
    while (len(base2) > 1):
        total += 1
        tmp = []
        for i in range(len(base2)):
            if base2[i] == '1':
                tmp.append((base2[i]))
            elif base2[i] == '0':
                cnt += 1     
        n = len(tmp)
        base2 = []
        while (n > 0):
            if n % 2 == 1:
                base2.append('1')
                n //= 2
            else:
                base2.append('0')
                n //= 2 
        base2.reverse()
        
    result = [total, cnt]
    return result