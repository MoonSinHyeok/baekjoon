import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())

city = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().rstrip("\n").split())
  city[a].append((c, b))

A, B = map(int, input().rstrip("\n").split())

# print("\n", *city, "\n", sep='\n')


def dijkstra(start):
  distance = [sys.maxsize] * (n + 1)
  distance[start] = 0
  visited = [False] * (n + 1)
  queue = []
  heappush(queue, (0, start))
  route = [[start] for _ in range(n + 1)]

  while queue:
    dist, idx = heappop(queue)
    if visited[idx]:
      continue
    visited[idx] = True
    for c, b in city[idx]:
      if distance[b] > dist + c:
        route[b] = route[idx] + [b]
        # print("node:", b, "dist:", dist + c, "route:", *route[b], sep=' ')
        distance[b] = dist + c
        heappush(queue, (distance[b], b))

  return distance, route


distance, route = dijkstra(A)
print(distance[B])
print(len(route[B]))
print(*(route[B]), sep=' ')
