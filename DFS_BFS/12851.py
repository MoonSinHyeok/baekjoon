from collections import deque

N, K = map(int, input().split())

short = 0
many = 0


def bfs(N, K):
  global short, many
  q = deque()
  q.append(N)
  visited = [0] * 200001
  while q:
    cur = q.popleft()

    if cur == K:
      short = visited[cur]
      many += 1
      continue
    else:
      for next in [cur + 1, cur - 1, cur * 2]:
        if 0 <= next <= 200000:
          if not visited[next] or visited[next] == visited[cur] + 1:
            visited[next] = visited[cur] + 1
            q.append(next)
  return


bfs(N, K)
print(short)
print(many)
