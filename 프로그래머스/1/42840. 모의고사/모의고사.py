def solution(answers):
    #1, 2, 3, 4, 5, 1, 2, 3, 4, 5
    #2, 1, 2, 3, 2, 4, 2, 5
    #3, 3, 1, 1, 2, 2, 4, 4, 5, 5
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    i = 0
    while i < len(answers):
        ans = answers[i]

        if ans == num_1[i % len(num_1)]:
            cnt_1 += 1
        if ans == num_2[i % len(num_2)]:
            cnt_2 += 1
        if ans == num_3[i % len(num_3)]:
            cnt_3 += 1

        i += 1

    max_cnt = max(cnt_1, cnt_2, cnt_3)
    answer = []
    
    if cnt_1 == max_cnt:
        answer.append(1)
    if cnt_2 == max_cnt:
        answer.append(2)
    if cnt_3 == max_cnt:
        answer.append(3)

    return answer
