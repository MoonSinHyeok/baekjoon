N, Q = map(int, input().split())

slot = [0] * N
for _ in range(Q):
  L, I = map(int, input().split())
  for i in range(L - 1, N, I):
    slot[i] = 1

ans = 0
for e in slot:
  if not e:
    ans += 1

print(ans)
