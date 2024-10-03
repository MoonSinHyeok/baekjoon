N = int(input())

dp = [['1']]

for i in range(1, N + 1):
  next = []
  carry = 0
  for j in range(len(dp[i - 1]) - 1, -1, -1):
    tmp = int(dp[i - 1][j]) * i + carry
    carry = tmp // 10
    remain = tmp % 10
    next.insert(0, str(remain))
  if carry:
    next.insert(0, str(carry))
  dp.append(next)

for e in dp[N]:
  print(e, end='')
