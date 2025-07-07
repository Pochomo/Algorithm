def solution(name, yearning, photo):
    answer = []
    for i in photo:
        point = 0
        for n in i:
            if n in name:
                point += yearning[name.index(n)]
        answer.append(point)
    return answer