import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    temp_id = []
    
    # 2단계
    for char in new_id:
        if re.match(r'[a-z0-9\-_\.]', char):
            temp_id.append(char)
    
    new_id = temp_id
    
    # 3단계
    index_point = 0
    i = 0
    while i < len(new_id):
        if new_id[i] == '.':
            index_point = i
            j = i + 1
            while j < len(new_id) and new_id[j] == '.':
                index_point = j
                j += 1
            if index_point > i:
                del new_id[i+1:index_point+1]
        i += 1
    
    # 4단계
    if new_id and new_id[0] == '.':
        del new_id[0]
    if new_id and new_id[-1] == '.':
        del new_id[-1]
    
    # 5단계
    if not new_id:
        new_id = ['a']
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            del new_id[-1]
    
    # 7단계
    while len(new_id) <= 2:
        new_id.append(new_id[-1])
    
    return ''.join(new_id)