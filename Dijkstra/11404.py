import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())

city = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().rstrip("\n").split())
  city[a].append((c, b))


def dijkstra(start, last, arr):
  distance = [sys.maxsize] * (last + 1)
  distance[start] = 0
  queue = []
  heappush(queue, (0, start))
  while queue:
    w, n = heappop(queue)
    if distance[n] < w:
      continue
    for weight, node in arr[n]:
      if weight + w < distance[node]:
        distance[node] = weight + w
        heappush(queue, (distance[node], node))

  for i in range(1, last + 1):
    if distance[i] == sys.maxsize:
      distance[i] = 0
  return distance[1:]


for i in range(1, n + 1):
  print(*dijkstra(i, n, city), sep=' ')
