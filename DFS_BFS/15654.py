import sys

input = sys.stdin.readline
N, M = map(int, input().split())

insert = []

li = list(map(int, input().rstrip('\n').split()))
for i in li:
  insert.append(i)

insert.sort()
seq = []


def dfs():
  global insert
  if len(seq) == M:
    print(' '.join(str(i) for i in seq))
    return
  for i in range(N):
    if insert[i] not in seq:
      seq.append(insert[i])
      dfs()
      seq.pop()


dfs()
