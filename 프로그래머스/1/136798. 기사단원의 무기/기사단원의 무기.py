def solution(number, limit, power):
    a = []
    for i in range(1, number+1):
        div = 0
        for j in range(1, int(i**(1/2))+1):
            if i % j == 0:
                div += 1
                if j**2 != i:
                    div += 1
            if div > limit:
                div = power
                break
        a.append(div)
    return sum(a)