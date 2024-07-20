import sys
from collections import deque

input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [1e6 for _ in range(N + 1)]
distance2 = [1e6 for _ in range(N + 1)]

for _ in range(M):
  S, E, T = map(int, input().split())
  graph[S].append((T, E))


def dijkstra(start):
  q = deque()
  q.append((0, start))
  distance[start] = 0
  while q:
    weight, node = q.popleft()
    if distance[node] < weight:
      continue

    for w, v in graph[node]:
      if distance[v] > distance[node] + w:
        distance[v] = distance[node] + w
        q.append((distance[node] + w, v))


def dijkstra2(start):
  global distance2
  q = deque()
  q.append((0, start))
  distance2[start] = 0
  while q:
    weight, node = q.popleft()
    if distance2[node] < weight:
      continue

    for w, v in graph[node]:
      if distance2[v] > distance2[node] + w:
        distance2[v] = distance2[node] + w
        q.append((distance2[node] + w, v))


dijkstra(X)
# print(distance)
ans = 0
for i in range(1, N + 1):
  dijkstra2(i)
  # print(distance2)
  if (distance[i] + distance2[X] > ans):
    ans = distance[i] + distance2[X]
  distance2 = [1e6 for _ in range(N + 1)]

print(ans)
