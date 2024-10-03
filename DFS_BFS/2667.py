import sys

input = sys.stdin.readline

N = int(input())
m = []
for _ in range(N):
  m.append(list(map(int, list(input().rstrip('\n')))))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * N for _ in range(N)]
tmp = 1


def dfs(x, y):
  global dx, dy, visited, tmp
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < N and 0 <= ny < N and m[nx][ny] == 1
        and not visited[nx][ny]):
      tmp += 1
      dfs(nx, ny)


ans = []
for i in range(N):
  for j in range(N):
    if m[i][j] == 1 and not visited[i][j]:
      dfs(i, j)
      ans.append(tmp)
    tmp = 1

print(len(ans))
print(*(sorted(ans)), sep='\n')
