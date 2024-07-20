import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []

for _ in range(H):
  tmp = []
  for _ in range(N):
    tmp.append(list(map(int, input().split())))
  box.append(tmp)

# 탐색 때 좌표 변화
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()  # 익을 토마토 좌표 들어갈 곳
li = []  # 좌표 저장용
ans = 0  # 답

for i in range(H):
  for j in range(N):
    for k in range(M):
      if box[i][j][k] == 1:
        li.append((k, j, i))

if li:  # 익은 토마토 좌표들
  q.append(li)

while q:  # 더이상 익을 토마토가 없을 때까지
  loc = q.popleft()
  li = []
  no = True
  for x, y, z in loc:
    for l in range(6):
      tx = x + dx[l]
      ty = y + dy[l]
      tz = z + dz[l]
      if ((0 <= tx < M) and (0 <= ty < N) and (0 <= tz < H)
          and box[tz][ty][tx] == 0):
        box[tz][ty][tx] = 1
        no = False  # 익게 된 토마토가 하나라도 있으면
        li.append((tx, ty, tz))
  if not no:
    q.append(li)
    ans += 1

for i in range(H):
  for j in range(N):
    for k in range(M):
      if box[i][j][k] == 0:
        print(-1)
        exit(0)

print(ans)
