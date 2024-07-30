N, M = map(int, input().split())

seq = []


def dfs(start):
  if len(seq) == M:
    print(' '.join(str(i) for i in seq))
    return
  for i in range(start, N + 1):
    seq.append(i)
    dfs(i + 1)
    seq.pop()


dfs(1)
