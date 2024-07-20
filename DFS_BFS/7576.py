import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = []
for _ in range(N):
  box.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]  # 좌우 확인
dy = [0, 0, 1, -1]  # 상하 확인
q = deque()  # 안익은 토마토(곧 익을) 좌표 리스트 저장할 큐
li = []  # 안익은 토마토 좌표 저장할 리스트
ans = 0  # 답

for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      li.append((j, i))

if li:
  q.append(li)

while q:
  list = q.popleft()
  li = []
  no = True
  for x, y in list:
    for k in range(4):
      tx = x + dx[k]
      ty = y + dy[k]
      if (0 <= tx < M) and (0 <= ty < N) and box[ty][tx] == 0:
        box[ty][tx] = 1
        no = False
        li.append((tx, ty))
  if not no:
    q.append(li)
    # print(li)
    ans += 1

for i in range(N):
  for j in range(M):
    if box[i][j] == 0:
      print(-1)
      exit(0)

print(ans)
