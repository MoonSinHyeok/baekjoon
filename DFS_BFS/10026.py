import sys

sys.setrecursionlimit(1000000)

N = int(input())
arr = []
for _ in range(N):
  arr.append(list(input()))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
check1 = [[0 for _ in range(N)] for _ in range(N)]  # 정상
check2 = [[0 for _ in range(N)] for _ in range(N)]  # 적록색맹
ans1 = 0
ans2 = 0


def dfs1(i, j):
  check1[i][j] = 1
  for k in range(4):
    tx = i + dx[k]
    ty = j + dy[k]
    if 0 <= tx < N and 0 <= ty < N and not check1[tx][ty] and arr[tx][
        ty] == arr[i][j]:
      dfs1(tx, ty)


def dfs2(i, j):
  check2[i][j] = 1
  if arr[i][j] == 'R' or arr[i][j] == 'G':
    for k in range(4):
      tx = i + dx[k]
      ty = j + dy[k]
      if 0 <= tx < N and 0 <= ty < N and not check2[tx][ty] and (
          arr[tx][ty] == 'R' or arr[tx][ty] == 'G'):
        dfs2(tx, ty)
  else:
    for k in range(4):
      tx = i + dx[k]
      ty = j + dy[k]
      if 0 <= tx < N and 0 <= ty < N and not check2[tx][ty] and arr[tx][
          ty] == 'B':
        dfs2(tx, ty)


for i in range(N):
  for j in range(N):
    if not check1[i][j]:
      dfs1(i, j)
      ans1 += 1
    if not check2[i][j]:
      dfs2(i, j)
      ans2 += 1

print(ans1, ans2)
