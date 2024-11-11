import sys

input = sys.stdin.readline
M = int(input())
li = []
for _ in range(M):
  li.append(list(map(int, input().split())))

mod = 1000000007
res = 0
for N, S in li:
  N_inv = pow(N, mod - 2, mod)
  res = (res + ((N_inv * S) % mod)) % mod

print(res)
