import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, land):
  if check[y][x]:
    return False
  check[y][x] = 1
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  for i in range(4):
    tx = x + dx[i]
    ty = y + dy[i]
    if (0 <= tx < M) and (0 <= ty < N) and land[ty][tx] == 1:
      dfs(tx, ty, land)
  return True


T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  land = [[0 for _ in range(M)] for _ in range(N)]
  check = [[0 for _ in range(M)] for _ in range(N)]
  # ex) M=4, N=3
  # [[0, 0, 0, 0],
  #  [0, 0, 0, 0],
  #  [0, 0, 0, 0]]

  cnt = 0
  for _ in range(K):
    x, y = map(int, input().split())
    land[y][x] = 1

  for i in range(N):
    for j in range(M):
      if land[i][j] and not check[i][j]:
        c = dfs(j, i, land)
        if c: cnt += 1

  print(cnt)
