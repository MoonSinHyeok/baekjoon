from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
check = [0] * 100001

while q:
  n = q.popleft()
  if n == K:
    print(check[n])
    break

  n1 = n + 1
  n2 = n - 1
  n3 = n * 2

  if 0 <= n1 <= 100000 and not check[n1]:
    q.append(n1)
    check[n1] = check[n] + 1
  if 0 <= n2 <= 100000 and not check[n2]:
    q.append(n2)
    check[n2] = check[n] + 1
  if 0 <= n3 <= 100000 and not check[n3]:
    q.append(n3)
    check[n3] = check[n] + 1
