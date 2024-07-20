import sys

input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().rstrip().split())) for _ in range(n)]
# dp
# 다음 층 선택: 현재 층 인덱스와 동일 or +1

dp = [[] for _ in range(n)]

for i in range(n):
  for e in triangle[i]:
    dp[i].append(e)

for i in range(1, n):
  for j in range(i + 1):
    if j == 0:
      dp[i][j] += dp[i - 1][j]
    elif j == i:
      dp[i][j] += dp[i - 1][j - 1]
    else:
      dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))
