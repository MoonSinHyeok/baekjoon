import sys

input = sys.stdin.readline

middle = input().rstrip("\n")

# ord(입력값) - ord(A) 범위가 0 ~ 24인경우 알파벳 대문자.
# 스택에 저장 일단 ㅇㅇ

stack = []
result = ""
for e in middle:
  if 0 <= ord(e) - ord('A') <= 25:
    result += e
  else:
    if e == '(':
      stack.append(e)
    elif e == '*' or e == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        result += stack.pop()
      stack.append(e)
    elif e == '+' or e == '-':
      while stack and stack[-1] != '(':
        result += stack.pop()
      stack.append(e)
    elif e == ')':
      while stack and stack[-1] != '(':
        result += stack.pop()
      stack.pop()

while stack:
  result += stack.pop()

print(result)
