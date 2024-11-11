import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
jido = []
for _ in range(N):
  jido.append(list(map(int, input().split())))

# for l in jido:
#   print(*l, sep=' ')

virus = []
for i in range(N):
  for j in range(M):
    if jido[i][j] == 2:
      virus.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
  # 아래 코드를 벽세우는 경우의 수만큼 반복
  global dx, dy, jido

  queue = deque()
  for v in virus:
    queue.append(v)
  # for e in queue:
  #   print(e)

  tmp = copy.deepcopy(jido)

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
        tmp[nx][ny] = 2
        queue.append((nx, ny))

  cnt = 0
  for i in range(N):
    for j in range(M):
      if tmp[i][j] == 0:
        cnt += 1
  return cnt


def backtracking(wall):
  global jido, ans
  if wall == 3:
    ans = max(ans, bfs())
    return

  for i in range(N):
    for j in range(M):
      if jido[i][j] == 0:
        jido[i][j] = 1
        backtracking(wall + 1)
        jido[i][j] = 0


ans = 0
backtracking(0)
print(ans)
