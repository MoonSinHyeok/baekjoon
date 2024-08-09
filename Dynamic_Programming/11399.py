import sys

input = sys.stdin.readline

N = int(input())
li = list(map(int, input().rstrip('\n').split()))

li.sort()
S = [0]
for e in li:
  S.append(S[-1] + e)

print(sum(S))
