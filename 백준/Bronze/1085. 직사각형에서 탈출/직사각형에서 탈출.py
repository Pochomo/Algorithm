#백준 1085 직사각형에서 탈출출 
x, y, w, h = map(int, input().split())
result = min(w-x, h-y, x-0, y-0)
print(result)