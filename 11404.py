import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

city = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

for i in range(m):
  a, b, c = map(int, input().rstrip("\n").split())
  if c < city[a][b]:
    city[a][b] = c


def dijkstra(start):
  distance = city[start]
  visited = [False] * (n + 1)
  visited[start] = True

  for _ in range(n):
    idx = distance.index(min(*distance))
    print(*distance[1:], sep=' ')
    print(idx, "\n\n")
    visited[idx] = True
    for i in range(1, n + 1):
      if not visited[i] and distance[i] > distance[idx] + city[idx][i]:
        distance[i] = distance[idx] + city[idx][i]

  for i in range(1, n + 1):
    if distance[i] == sys.maxsize:
      distance[i] = 0


for i in range(1, n + 1):
  dijkstra(i)

for i in range(1, n + 1):
  city[i][i] = 0

for e in city[1:]:
  print(*(e[1:]), sep=' ')
