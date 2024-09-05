import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
  a, b = map(int, input().rstrip('\n').split())
  tree[a].append(b)
  tree[b].append(a)

parent = [0] * (N + 1)


def bfs(start):
  visited = [False] * (N + 1)
  queue = [start]
  while queue:
    node = queue.pop(0)
    visited[node] = True
    for n in tree[node]:
      if not visited[n]:
        queue.append(n)
        parent[n] = node


bfs(1)
print(*parent[2:], sep='\n')
