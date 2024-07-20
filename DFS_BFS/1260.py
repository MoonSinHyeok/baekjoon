import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
check = [0 for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1


def dfs(v, check):
  check[v] = 1
  print(v, end=' ')
  for i in range(1, N + 1):
    if not check[i] and graph[v][i]:
      dfs(i, check)


def bfs(v, check):
  queue = [v]
  check[v] = 1
  while queue:
    v = queue.pop(0)
    print(v, end=' ')
    for i in range(1, N + 1):
      if not check[i] and graph[v][i]:
        queue.append(i)
        check[i] = 1


dfs(V, check)
print()
check = [0 for _ in range(N + 1)]
bfs(V, check)
