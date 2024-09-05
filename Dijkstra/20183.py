import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M, A, B, C = map(int, input().rstrip("\n").split())

graph = [[] * (N+1)]

for _ in range(M):
  a, b, c = map(int, input().rstrip("\n").split())
  graph[a].append((c, b))
  graph[b].append((c, a))

def dijkstra(start):
  # 자...
  # 