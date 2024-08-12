import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().rstrip("\n").split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, input().rstrip("\n").split())
  graph[a][b] = 1
  graph[b][a] = 1

cnt = 0


def dfs(start):
  visited[start] = 1
  for i in range(1, N + 1):
    if graph[start][i] == 1 and visited[i] == 0:
      dfs(i)


node = 1
while 1:
  dfs(node)
  cnt += 1
  for i in range(1, N + 1):
    if visited[i] == 0:
      node = i
      break
  else:
    break

print(cnt)
