from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
maze = []
for _ in range(N):
  maze.append(list(map(int, list(input().rstrip('\n')))))

# print(*maze, sep='\n')


def bfs(x, y):
  queue = deque()
  queue.append((x, y, 1))
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  visited = [[False] * M for _ in range(N)]
  visited[x][y] = True
  while queue:
    a, b, dist = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if (0 <= nx < N and 0 <= ny < M and not visited[nx][ny]
          and maze[nx][ny] == 1):
        if nx == N - 1 and ny == M - 1:
          return dist + 1
        queue.append((nx, ny, dist + 1))
        visited[nx][ny] = True


print(bfs(0, 0))
