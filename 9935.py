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

  if c == explosion[cursor]:
    # print(start_check)
    # print(ans)
    if cursor == 0:
      start_check.append(len(ans) - 1)
    cursor += 1
    if cursor == len(explosion):
      cursor = 0
      for _ in range(len(explosion)):
        ans.pop()

      if start_check:
        for i in range(start_check[-1], len(ans)):
          if ans[i] == explosion[cursor]:
            cursor += 1
          else:
            cursor = 0
            break
        else:
          start_check.pop()
  else:
    cursor = 0

if ans:
  print(''.join(ans))
else:
  print("FRULA")
