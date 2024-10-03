import sys

input = sys.stdin.readline

# dp 점화식을 생각해보자...
# 한칸씩 오른다면 dp[i][1] = dp[i-1][1] + 1 만약 이값이 3이 된다면 한칸씩 오르면 안됨
# 두칸씩 오른다면 dp[i][1] = 1 로 초기화
# dp[i][0]은 dp[i-1][0]과 dp[i-2][0] 중 큰것과 현재 계단(i)의 합

# ---> 틀림..
# 수정: 애초에 dp[i-1]을 활용하지 말고 dp[i-2]와 dp[i-3]과 stair[i-1]을 더한값을 비교하여 큰값을 넣으면 됐음

N = int(input())
stair = []
for _ in range(N):
  stair.append(int(input()))

dp = []
if N == 1:
  print(stair[0])
elif N == 2:
  print(stair[0] + stair[1])
else:
  dp.append(stair[0])
  dp.append(stair[0] + stair[1])
  dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
  for i in range(3, N):
    dp.append(max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i])
  print(dp[N - 1])
