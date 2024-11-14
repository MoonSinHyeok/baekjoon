from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  build_time = [0] + list(map(int, input().split()))
  building = [[] for _ in range(N + 1)]
  order = [0] * (N + 1)
  dp = [0] * (N + 1)

  for _ in range(K):
    x, y = map(int, input().split())
    building[x].append(y)
    order[y] += 1
  W = int(input())
  # 데이터 입력 끝

  # 위상정렬
  q = deque()
  for i in range(N + 1):
    if order[i] == 0:
      q.append(i)
      dp[i] = build_time[i]

  while q:
    now = q.popleft()
    for e in building[now]:
      order[e] -= 1
      dp[e] = max(dp[now] + build_time[e], dp[e])
      if order[e] == 0:
        q.append(e)

  print(dp[W])
