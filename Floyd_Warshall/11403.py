import sys

input = sys.stdin.readline

N = int(input())
G = []

for _ in range(N):
  G.append(list(map(int, input().split())))

for k in range(N):
  for i in range(N):
    for j in range(N):
      if G[i][k] == 1 and G[k][j] == 1:
        G[i][j] = 1

for l in G:
  for e in l:
    print(e, end=' ')
  print()
