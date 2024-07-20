import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))


def find_max(l):
  r = 0
  for i in l:
    if (i > r):
      r = i
  return r


max = find_max(scores)

sum = 0
for i in scores:
  sum += i

average = sum * 100 / max / n
print(average)
