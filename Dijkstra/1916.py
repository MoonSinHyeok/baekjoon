import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
M = int(input())

city = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip("\n").split())
    city[a].append((c, b))

start, end = map(int, input().rstrip("\n").split())


def dijkstra(start):
    distance = [sys.maxsize] * (N + 1)
    distance[start] = 0
    visited = [False] * (N + 1)
    queue = []
    heappush(queue, (0, start))

    while queue:
        weight, node = heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        for w, n in city[node]:
            if not visited[n] and weight + w < distance[n]:
                distance[n] = weight + w
                heappush(queue, (distance[n], n))
    return distance


print(dijkstra(start)[end])
