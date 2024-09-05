# 1504 feat .python

import sys
from heapq import heappush, heappop


input = sys.stdin.readline

N, E = map(int, input().rstrip("\n").split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip("\n").split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().rstrip("\n").split())

def dijkstra(start):
  distance = [sys.maxsize] * (N+1)
  distance[start] = 0
  visited = [False] * (N+1)
  queue = []
  heappush(queue, (0, start))
  while queue:
    w, n = heappop(queue)
    visited[n] = True
    for weight, node in graph[n]:
      if visited[node] == False and w + weight < distance[node]:
        distance[node] = w + weight
        heappush(queue, (distance[node], node))

  return distance

dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(v2)

check_list1 = [dist1[v1], dist2[v2], dist3[N]]
check_list2 = [dist1[v2], dist3[v1], dist2[N]]

flag1 = False
flag2 = False
for e in check_list1:
    if e == sys.maxsize:
        flag1 = True

for e in check_list2:
    if e == sys.maxsize:
        flag2 = True



if flag1 and flag2:
    print(-1)
else:
    case1 = dist1[v1] + dist2[v2] + dist3[N]
    case2 = dist1[v2] + dist3[v1] + dist2[N]
    print(case1 if case1 < case2 else case2)
