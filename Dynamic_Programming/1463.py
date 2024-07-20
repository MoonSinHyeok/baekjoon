N = int(input())

dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
  tmp1 = 0
  tmp2 = N
  tmp3 = N

  tmp1 = dp[i - 1] + 1

  if i % 2 == 0:
    tmp2 = dp[i // 2] + 1

  if i % 3 == 0:
    tmp3 = dp[i // 3] + 1

  dp[i] = min(tmp1, tmp2, tmp3)

  # print(f"dp[{i}] = {dp[i]}")

print(dp[N])
