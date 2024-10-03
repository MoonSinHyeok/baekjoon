import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())

board = [0] * 101
for _ in range(N):
  x, y = map(int, input().rstrip('\n').split())
  board[x] = y

for _ in range(M):
  u, v = map(int, input().rstrip('\n').split())
  board[u] = v


def bfs(start):
  queue = [start]
  visited = [0] * 101
  while queue:
    cur = queue.pop(0)

    warp = board[cur]
    if warp:
      visited[warp] = visited[cur]
      cur = warp

    for i in range(1, 7):
      tmp = cur + i
      if tmp < 101 and not visited[tmp]:
        # print(tmp, visited[cur])
        queue.append(tmp)
        visited[tmp] = visited[cur] + 1
      if tmp == 100:
        return visited[cur] + 1


print(bfs(1))
