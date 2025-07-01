def solution(s):
    word_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    result = ""
    i = 0
    while i < len(s):
        found = False
        for word in word_to_number:
            word_len = len(word)
            if i + word_len <= len(s) and s[i:i+word_len] == word:
                result += word_to_number[word]
                i += word_len
                found = True
                break
        
        if not found:
            result += s[i]
            i += 1
    
    return int(result)