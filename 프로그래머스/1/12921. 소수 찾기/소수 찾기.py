def solution(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    limit = int(n ** 0.5)
    for p in range(2, limit + 1):
        if prime[p]:
            prime[p*p : n+1 : p] = [False] * len(range(p*p, n+1, p))

    return sum(prime)