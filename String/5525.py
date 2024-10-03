import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip('\n')

P = "IOI"

ans = 0
cnt = 0
i = 0
while i < M - 1:
  if S[i:i + 3] == P:
    i += 2
    cnt += 1
    if cnt == N:
      ans += 1
      cnt -= 1
  else:
    i += 1
    cnt = 0

print(ans)

# li = [0] * len(P)
# pi = 0
# for i in range(1, len(P)):
#   while pi > 0 and P[pi] != P[i]:
#     pi = li[pi - 1]
#   if P[pi] == P[i]:
#     pi += 1
#     li[i] = pi

# # kmp
# pi = 0
# for i in range(len(S)):
#   while pi > 0 and P[pi] != S[i]:
#     pi = li[pi - 1]
#   if P[pi] == S[i]:
#     if pi == len(P) - 1:
#       ans += 1
#       pi = li[pi]
#     else:
#       pi += 1

# for i in range(M - len(P) + 1):
#   if S[i] == "I":
#     # print(S[i:])
#     for j in range(len(P)):
#       if (S[i:])[j] == P[j]:
#         continue
#       else:
#         break
#     else:
#       ans += 1

# print(ans)
