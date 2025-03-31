#백준 20300 서강근육맨
INF = 10**19
n = int(input())
muscle = list(map(int, input().split()))

muscle.sort()
m = muscle[n-1]
if len(muscle) % 2 == 0:
    for i in range(0, n//2):
        m = max(m, muscle[i] + muscle[n-i-1])
else:
    for i in range(0, n//2 + 1):
        m = max(m, muscle[i] + muscle[n-i-2])
        
print(m)