def solution(s):
    result = []
    first_word = True

    for char in s:
        if first_word:
            result.append(char.upper() if char.isalpha() else char)
            first_word = False
        else:
            result.append(char.lower())
        if char == " ":
            first_word = True

    return "".join(result)
