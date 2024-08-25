import sys

input = sys.stdin.readline

K = int(input())


def bfs(start):
  queue = [start]
  while queue:
    v = queue.pop(0)
    if visited[v] == 0:
      for e in graph[v]:
        if visited[e] != 0:
          visited[v] = visited[e] * -1
          break
      else:
        visited[v] = 1
    for e in graph[v]:
      if visited[e] != 0:
        if visited[v] == visited[e]:
          return False
        continue
      visited[e] = visited[v] * -1
      queue.append(e)
  return True


for _ in range(K):
  V, E = map(int, input().rstrip("\n").split())

  graph = [[] for _ in range(V + 1)]
  for _ in range(E):
    a, b = map(int, input().rstrip("\n").split())
    graph[a].append(b)
    graph[b].append(a)

  visited = [0] * (V + 1)
  check = True
  for i in range(1, V + 1):
    if not check:
      print("NO")
      break
    if visited[i] == 0:
      check = bfs(i)
  else:
    print("YES")
