import sys

input = sys.stdin.readline

com = int(input())
pair = int(input())

network = [[0] * (com + 1) for _ in range(com + 1)]
for _ in range(pair):
  a, b = map(int, input().rstrip("\n").split())
  network[a][b] = 1
  network[b][a] = 1


def bfs(start):
  queue = [start]
  visited = [0] * (com + 1)
  visited[start] = 1
  while queue:
    now = queue.pop(0)
    for i in range(1, com + 1):
      if network[now][i] and not visited[i]:
        queue.append(i)
        visited[i] = 1
  return sum(visited) - 1


print(bfs(1))
