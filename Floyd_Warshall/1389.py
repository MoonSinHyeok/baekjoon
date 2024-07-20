import sys

input = sys.stdin.readline
N, M = map(int, input().split())

short = [[N for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  short[a][b] = short[b][a] = 1

for i in range(N + 1):
  short[i][i] = 0

for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      short[i][j] = min(short[i][j], short[i][k] + short[k][j])

ans = [0]
tmp = N**2
for i in range(1, N + 1):
  ans.append(sum(short[i]))
  if tmp > ans[i]:
    tmp = ans[i]

for i in range(1, N + 1):
  if ans[i] == tmp:
    print(i)
    break
