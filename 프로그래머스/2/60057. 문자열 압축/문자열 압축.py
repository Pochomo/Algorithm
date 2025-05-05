def solution(s):
    if len(s) == 1:
        return 1
    answer = float('inf')
    # 잘라서 넣으면서 같으면 숫자로 변환 아니면 계속 넣는다.
    for i in range(1, len(s)//2 + 1):
        stack = []
        temp_s = s

        for j in range(0, len(s), i):
            current = temp_s[j:j+i]
            
            if not stack:
                stack.append([current, 1])
            elif stack[-1][0] == current:
                stack[-1][1] += 1
            else:
                stack.append([current, 1])
                
        ans = ''
        for string, cnt in stack:
            if cnt > 1:
                ans += str(cnt) + string
            else:
                ans += string
                    
        answer = min(len(ans), answer)
    return answer