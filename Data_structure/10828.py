import sys

input = sys.stdin.readline

li = []
N = int(input())
for _ in range(N):
  order = input().rstrip("\n")
  if order[:4] == "push":
    li.append(int(order[5:]))
  elif order == "pop":
    if len(li) == 0:
      print(-1)
    else:
      print(li.pop())
  elif order == "size":
    print(len(li))
  elif order == "empty":
    if len(li) == 0:
      print(1)
    else:
      print(0)
  elif order == "top":
    if li:
      print(li[-1])
    else:
      print(-1)
