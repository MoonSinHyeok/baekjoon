import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, M = map(int, input().rstrip("\n").split())

  bad = [[] for _ in range(N+1)]
  inserted = [[False] * (N+1) for _ in range(2)]
  for i in range(M):
    a, b = map(int, input().rstrip("\n").split())
    bad[a].append(b)
    bad[b].append(a)
    
  for i in range(1, N+1):
    if not inserted[0][i] and not inserted[1][i]:
      inserted[0][i] = True
      for j in bad[i]:
        if not inserted[0][j] and not inserted[1][j]:
          inserted[1][j] = True
        else:
          inserted[1][j] = True