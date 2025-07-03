def solution(strings, n):
    # n번째 인덱스 기준으로 정렬
    strings.sort(key=lambda x: (x[n], x))
    return strings