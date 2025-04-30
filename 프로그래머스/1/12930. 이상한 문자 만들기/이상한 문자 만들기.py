def solution(s):
    words = s.split(' ')
    
    for i in range(len(words)):
        if words[i] == '':
            continue
            
        result = ''
        for j in range(len(words[i])):
            if j % 2 == 0:
                result += words[i][j].upper()
            else:
                result += words[i][j].lower()
        words[i] = result
    
    return ' '.join(words)