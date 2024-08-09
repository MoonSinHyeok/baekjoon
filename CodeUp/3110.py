N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]
ans = li.pop(0)

while li:
  for _ in range(K - 1):
    li.append(li.pop(0))
  ans = li.pop(0)
print(ans)
