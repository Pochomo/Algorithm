def solution(word):
    answer = -1
    clist = []
    a_list = ['A', 'E', 'I', 'O', 'U']
    
    while True:
        current_word = ''.join(clist)
        answer += 1
        
        if current_word == word:
            return answer
        
        if len(clist) < 5:
            clist.append('A')
        else:
            while clist:
                last_char = clist.pop()
                last_idx = a_list.index(last_char)

                if last_idx < 4:
                    clist.append(a_list[last_idx + 1])
                    break
            else:
                break

    return answer