import sys

input = sys.stdin.readline

dict = {}
N = int(input())
for e in map(int, input().rstrip("\n").split()):
  if e not in dict:
    dict[e] = 1
  else:
    dict[e] += 1

M = int(input())

for e in map(int, input().rstrip("\n").split()):
  if e in dict:
    print(dict[e], end=" ")
  else:
    print(0, end=" ")
