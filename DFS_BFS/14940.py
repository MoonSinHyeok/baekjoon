import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
m = []
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(N):
  m.append(list(map(int, input().split())))

definition = [(-1, -1)]
for i in range(N):
  for j in range(M):
    if m[i][j] == 2:
      definition = [(j, i)]
      visited[i][j] = 1
      m[i][j] = 0

q = deque()
q.append(definition)

distance = 1
while q:
  li = q.popleft()
  tmp = []
  for x, y in li:
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if (0 <= tx < M and 0 <= ty < N and not visited[ty][tx]
          and m[ty][tx] == 1):
        visited[ty][tx] = 1
        m[ty][tx] = distance
        tmp.append((tx, ty))
  if tmp:
    q.append(tmp)
  distance += 1

# 갈 수 있는 땅이면서 도달할 수 없는 위치
x = definition[0][0]
y = definition[0][1]
for i in range(4):
  tx = x + dx[i]
  ty = y + dy[i]
  if (0 <= tx < M and 0 <= ty < N and m[ty][tx] != 0):
    m[ty][tx] = -2

for i in range(N):
  for j in range(M):
    if m[i][j] == 1:
      m[i][j] = -1

for i in range(4):
  tx = x + dx[i]
  ty = y + dy[i]
  if (0 <= tx < M and 0 <= ty < N and m[ty][tx] == -2):
    m[ty][tx] = 1
###################################

# print()
for i in range(N):
  for j in range(M):
    print(m[i][j], end=" ")
  print()
