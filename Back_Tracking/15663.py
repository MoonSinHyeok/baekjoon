import sys

input = sys.stdin.readline

N, M = map(int, input().split())
insert = []
for i in list(map(int, input().rstrip('\n').split())):
  insert.append(i)

insert.sort()

seq = []
visited = [0] * N


def dfs():
  if len(seq) == M:
    print(' '.join(str(i) for i in seq))
    return
  check = 0
  for i in range(N):
    if not visited[i] and check != insert[i]:
      visited[i] = 1
      seq.append(insert[i])
      check = insert[i]
      dfs()
      visited[i] = 0
      seq.pop()


dfs()
