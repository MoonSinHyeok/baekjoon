import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [float("inf") for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))  # 가중치, 노드 순 저장(우선순위 큐에서 가중치 기준으로 정렬)


def dijkstra(start):
  q = PriorityQueue()
  q.put((0, start))
  distance[start] = 0
  while not q.empty():
    weight, node = q.get()
    if distance[node] < weight:
      continue

    for w, v in graph[node]:
      if distance[v] > distance[node] + w:
        distance[v] = distance[node] + w
        q.put((distance[node] + w, v))


dijkstra(K)
for i in range(1, V + 1):
  print("INF" if distance[i] == float("inf") else distance[i])
