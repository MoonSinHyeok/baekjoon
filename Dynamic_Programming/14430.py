import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split())
mine = []
for _ in range(N):
  mine.append(list(map(int, input().rstrip("\n").split())))

for i in range(1, M):
  mine[0][i] += mine[0][i - 1]
for i in range(1, N):
  mine[i][0] += mine[i - 1][0]

for i in range(1, N):
  for j in range(1, M):
    mine[i][j] += max(mine[i - 1][j], mine[i][j - 1])

# print(*mine, sep="\n")
print(mine[N - 1][M - 1])
