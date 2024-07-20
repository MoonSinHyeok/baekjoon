N = int(input())

dp1 = [[], [0, 0, 0]]
dp2 = [[], [0, 0, 0]]

first = list(map(int, input().split()))
for e in first:
  dp1[0].append(e)
  dp2[0].append(e)

for i in range(1, N):
  next = list(map(int, input().split()))
  dp1[1][0] = max(dp1[0][0], dp1[0][1]) + next[0]
  dp1[1][1] = max(dp1[0][0], dp1[0][1], dp1[0][2]) + next[1]
  dp1[1][2] = max(dp1[0][1], dp1[0][2]) + next[2]

  dp2[1][0] = min(dp2[0][0], dp2[0][1]) + next[0]
  dp2[1][1] = min(dp2[0][0], dp2[0][1], dp2[0][2]) + next[1]
  dp2[1][2] = min(dp2[0][1], dp2[0][2]) + next[2]
  for j in range(3):
    dp1[0][j] = dp1[1][j]
  for j in range(3):
    dp2[0][j] = dp2[1][j]
    
print(max(dp1[0]), min(dp2[0]))