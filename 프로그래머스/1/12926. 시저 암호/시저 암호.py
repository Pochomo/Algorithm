def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif 'A' <= i <= 'Z':
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    return answer
