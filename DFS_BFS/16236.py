import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Ocean = []
for _ in range(N):
  Ocean.append(list(map(int, input().rstrip('\n').split())))

shark = (0, 0, 0)
for i in range(N):
  for j in range(N):
    if Ocean[i][j] == 9:
      shark = (j, i, 2)  # 위치(x, y), 크기

# 상 좌 우 하 순서로 탐색
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def bfs(start):
  visited = [[0] * N for _ in range(N)]
  q = deque()
  q.append(start)
  find = []

  visited[start[1]][start[0]] = 1

  while q:
    x, y, size = q.popleft()
    for i in range(4):
      ty, tx = y + dy[i], x + dx[i]
      if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
        if 0 < Ocean[ty][tx] < size:
          visited[ty][tx] = visited[y][x] + 1
          find.append((tx, ty, size, visited[ty][tx] - 1))
        elif Ocean[ty][tx] == size or Ocean[ty][tx] == 0:
          visited[ty][tx] = visited[y][x] + 1
          q.append((tx, ty, size))

  if find:
    find = sorted(find, key=lambda x: (x[3], x[1], x[0]))
  return find


cnt = 0
fish = 0
Ocean[shark[1]][shark[0]] = 0

while True:
  find = bfs(shark)
  if not find:
    break

  find = find[0]

  x, y, size, sec = find
  cnt += sec
  fish += 1
  if size == fish:
    size += 1
    fish = 0

  Ocean[y][x] = 0
  shark = (x, y, size)

  # print("[", x, y, size, fish, sec, "]")
  # for i in range(N):
  #   for e in Ocean[i]:
  #     print(e, end=" ")
  #   print()

print(cnt)
