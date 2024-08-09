# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys

input = sys.stdin.readline

S = set([])
M = int(input())

for _ in range(M):
  order = input().rstrip("\n")
  if order == "all":
    S = set([i for i in range(1, 21)])
  elif order == "empty":
    S = set([])
  elif order[:3] == "add":
    S.add(int(order[4:]))
  elif order[:5] == "check":
    if int(order[6:]) in S:
      print(1)
    else:
      print(0)
  elif order[:6] == "remove":
    S.discard(int(order[7:]))
  elif order[:6] == "toggle":
    if int(order[7:]) in S:
      S.discard(int(order[7:]))
    else:
      S.add(int(order[7:]))
