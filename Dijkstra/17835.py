import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, K = map(int, input().rstrip("\n").split())

city = [[] for _ in range(N + 1)]

for _ in range(M):
  U, V, C = map(int, input().rstrip("\n").split())
  city[V].append((C, U))

spots = []
line = list(input().rstrip("\n").split())
for e in line:
  spots.append(int(e))


def dijkstra(start):
  distance = [sys.maxsize] * (N + 1)
  distance[start] = 0
  queue = []
  heappush(queue, (0, start))
  while queue:
    w, n = heappop(queue)
    if distance[n] < w:
      continue
    for weight, node in city[n]:
      if distance[node] > w + weight:
        distance[node] = w + weight
        heappush(queue, (distance[node], node))
  # print(distance)
  return distance


def dijkstra2(spots):
  distance = [sys.maxsize] * (N + 1)
  for e in spots:
    distance[e] = 0
    queue = []
    heappush(queue, (0, e))
    while queue:
      w, n = heappop(queue)
      if distance[n] < w:
        continue
      for weight, node in city[n]:
        if distance[node] > w + weight:
          distance[node] = w + weight
          heappush(queue, (distance[node], node))
    # print(distance)
  return distance


# save = [sys.maxsize] * (N + 1)
# for spot in spots:
#   dist = dijkstra(spot)
#   for i in range(1, N + 1):
#     if save[i] > dist[i]:
#       save[i] = dist[i]

# node = None
# ans = 0

# for i in range(1, N + 1):
#   if save[i] != sys.maxsize and save[i] > ans:
#     node = i
#     ans = save[i]

# print(save)

dist = dijkstra2(spots)
ans = 0
node = None
for i in range(1, N + 1):
  if dist[i] > ans:
    node = i
    ans = dist[i]

print(node)
print(ans)
