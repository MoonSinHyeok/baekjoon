# 구간 합 구하기 5
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
  line = list(map(int, input().split()))
  for j in range(1, N + 1):
    arr[i][j] = line[j - 1]

for i in range(1, N + 1):
  for j in range(1, N + 1):
    sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + arr[i][j]

for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1])
