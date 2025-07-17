def solution(s):
    result = []
    first_word = True

    for char in s:
        if first_word:
            # 알파벳이고 대문자로 만들고 append
            result.append(char.upper() if char.isalpha() else char)
            first_word = False
        else:
            result.append(char.lower())
        if char == " ":
            first_word = True

    return "".join(result)
