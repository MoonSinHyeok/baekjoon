TC = int(input())
for _ in range(TC):
  N, M, W = map(int, input().split())

  node = [[] for _ in range(N + 1)]
  distance = [1e9 for _ in range(N + 1)]

  for _ in range(M):
    S, E, T = map(int, input().split())
    node[S].append((E, T))
    node[E].append((S, T))

  for _ in range(W):
    S, E, T = map(int, input().split())
    node[S].append((E, -T))

  check = False

  for i in range(1, N + 1):
    for s in range(1, N + 1):
      for e, t, in node[s]:
        if distance[e] > distance[s] + t:
          distance[e] = distance[s] + t
          if i == N:
            check = True

  if check:
    print("YES")
  else:
    print("NO")
