import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())
q = PriorityQueue()

for i in range(N):
  sel = int(input())
  if sel == 0:
    if q.empty():
      print(0)
    else:
      print(q.get()[1])
  else:
    q.put((abs(sel), sel))
