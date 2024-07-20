import sys

input = sys.stdin.readline

V = int(input())
edge = [[] for _ in range(V + 1)]
for _ in range(V):
  line = list(input().split())
  n = int(line[0])
  for j in range(1, len(line), 2):
    if int(line[j]) == -1:
      break
    edge[n].append((int(line[j]), int(line[j + 1])))

visited = [0 for _ in range(V + 1)]

## 전처리 끝

distance = 0
node = 0


def dfs(start, weight):
  global distance, node
  visited[start] = 1

  if distance < weight:
    distance = weight
    node = start

  for n, w in edge[start]:
    if not visited[n]:
      dfs(n, weight + w)


dfs(1, 0)

visited = [0 for _ in range(V + 1)]
dfs(node, 0)

print(distance)
