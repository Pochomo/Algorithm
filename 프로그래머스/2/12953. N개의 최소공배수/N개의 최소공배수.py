def gcd(a, b):
    while b:
        r = a % b
        a, b = b, r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans