#1715 카드 정렬하기
import sys
import heapq

input = sys.stdin.readline

n = int(input())

cards = []

for i in range(n):
    heapq.heappush(cards, int(input()))

costs = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    temp = a + b
    costs += temp
    heapq.heappush(cards, temp)

print(costs)