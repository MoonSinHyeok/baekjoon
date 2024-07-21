from collections import deque

# 문자열 입력받고 하나씩 큐에 넣으면서 확인해보자
str = input()
ans = deque()

# 폭발 문자열
explosion = input()
cursor = 0

# 폭발 문자열의 첫째 문자를 발견했을시 인덱스 저장
start_check = deque()

for c in str:
  ans.append(c)
  # print(start_check)
  # print(ans)
  # print()
  if c == explosion[0] != explosion[cursor]:
    cursor = 0
  if c == explosion[cursor]:
    if cursor == 0:
      if len(explosion) == 1:
        ans.pop()
        continue
      start_check.append(len(ans) - 1)
    cursor += 1
    if cursor == len(explosion):
      cursor = 0
      for _ in range(len(explosion)):
        ans.pop()
      start_check.pop()
      if start_check:
        tmp = 0
        for i in range(start_check[-1], len(ans)):
          if ans[i] == explosion[tmp]:
            tmp += 1
          else:
            break
        else:
          cursor = tmp
  else:
    cursor = 0

if ans:
  print(''.join(ans))
else:
  print("FRULA")
