# 구간 합 구하기 4
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
S = [0] * (N + 1)

for i in range(1, N + 1):
  S[i] = S[i - 1] + nums[i - 1]

result = []
for _ in range(M):
  i, j = map(int, input().split())
  result.append(S[j] - S[i - 1])

for i in result:
  print(i)
