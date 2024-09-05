import sys
from collections import deque

N, K = map(int, input().split())


def bfs(start):
  dist = [sys.maxsize] * 200001
  dist[start] = 0
  queue = deque()
  queue.append(start)
  while queue:
    loc = queue.popleft()
    if loc == K:
      return dist[loc]
    if loc * 2 <= 200000 and dist[loc] < dist[loc * 2]:
      dist[loc * 2] = dist[loc]
      queue.appendleft(loc * 2)
    if loc + 1 <= K and dist[loc] + 1 < dist[loc + 1]:
      dist[loc + 1] = dist[loc] + 1
      queue.append(loc + 1)
    if loc - 1 >= 0 and dist[loc] + 1 < dist[loc - 1]:
      dist[loc - 1] = dist[loc] + 1
      queue.append(loc - 1)


print(bfs(N))
