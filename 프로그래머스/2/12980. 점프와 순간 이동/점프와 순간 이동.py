def solution(n):
    ans = 0
    while n > 0:
        tmp = n % 2
        ans += tmp
        n //= 2

    return ans