import sys
from collections import deque

input = sys.stdin.readline


# bfs
def solution(num, find):
  q = deque()
  q.append((num, ""))

  while q:
    num, order = q.popleft()

    if num == find:
      print(order)
      break
    
    for sel in ['D', 'S', 'L', 'R']:
      tmp = num
      if sel == 'D':
        tmp = num * 2 % 10000
      if sel == 'S':
        tmp = (num - 1) % 10000
      if sel == 'L':
        tmp = (num % 1000) * 10 + num // 1000
      if sel == 'R':
        tmp = (num % 10) * 1000 + num // 10
      if tmp not in check:
        q.append((tmp, order + sel))
        check.add(tmp)


T = int(input())
for _ in range(T):
  check = set()
  num, find = map(int, input().split())
  solution(num, find)
