import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip("\n").split())
trees = list(map(int, input().rstrip("\n").split()))

trees.sort()
max = trees[-1]
min = 0
mid = (max + min) // 2
ans = 0

while min < max:
  cnt = 0
  mid = (max + min) // 2

  for tree in trees:
    cnt += (tree - mid) if tree >= mid else 0

  if cnt == M:
    ans = mid
    break
  elif cnt > M:
    ans = mid
    min = mid + 1
  else:
    max = mid

print(ans)
