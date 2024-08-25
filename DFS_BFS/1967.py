import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000000)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  p, c, w = map(int, input().rstrip("\n").split())
  tree[p].append((w, c))
  tree[c].append((w, p))

visited = [-1] * (n + 1)


def dfs(start, weight):
  for child in tree[start]:
    if visited[child[1]] == -1:
      visited[child[1]] = weight + child[0]
      dfs(child[1], weight + child[0])


visited[1] = 0
dfs(1, 0)
node = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[node] = 0
dfs(node, 0)

print(max(visited))
