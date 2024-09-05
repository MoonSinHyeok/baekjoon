import sys
from heapq import heappush, heappop

input = sys.stdin.readline

M, N = map(int, input().rstrip("\n").split())

maze = []
for _ in range(N):
  line = input().rstrip("\n")
  tmp = []
  for e in line:
    tmp.append(int(e))
  maze.append(tmp)


# print(*maze, sep=' ')

def dijkstra():
  distance = [[sys.maxsize] * (M) for _ in range(N)]
  distance[0][0] = 0
  queue = []
  heappush(queue, (0, (0, 0)))
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  while queue:
    w, (x, y) = heappop(queue)
    if distance[x][y] < w:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] > distance[x][y] + maze[nx][ny]:
        distance[nx][ny] = distance[x][y] + maze[nx][ny]
        heappush(queue, (distance[nx][ny], (nx, ny)))
  return distance[N-1][M-1]

print(dijkstra())