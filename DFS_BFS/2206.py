import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split())

arr = []
for i in range(N):
  arr.append(list(map(int, input().rstrip("\n"))))

# for e in arr:
#   print(*e, sep=' ')

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs(a, b, c):
  queue = deque()
  queue.append((a, b, c))

  while queue:
    a, b, c = queue.popleft()
    if a == N - 1 and b == M - 1:
      return visited[a][b][c]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
      tx = a + dx[i]
      ty = b + dy[i]
      if 0 <= tx <= N - 1 and 0 <= ty <= M - 1:
        if arr[tx][ty] == 1 and c == 0:
          visited[tx][ty][1] = visited[a][b][0] + 1
          queue.append((tx, ty, 1))
        elif arr[tx][ty] == 0 and not visited[tx][ty][c]:
          visited[tx][ty][c] = visited[a][b][c] + 1
          queue.append((tx, ty, c))

  return -2


print(bfs(0, 0, 0) + 1)

# for e in visited:
#   for e2 in e:
#     print(*e2, sep='/', end=' ')
#   print()
