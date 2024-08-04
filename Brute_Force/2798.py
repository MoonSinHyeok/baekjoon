import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
li = list(map(int, input().rstrip('\n').split()))
li.sort()

sum = 0
for i in range(N):
  for j in range(N):
    for k in range(N):
      if i != j and j != k and k != i:
        if sum < li[i] + li[j] + li[k] <= M:
          sum = li[i] + li[j] + li[k]

print(sum)
