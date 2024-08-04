import sys

input = sys.stdin.readline

while True:
  tri = list(map(int, input().rstrip('\n').split()))
  if tri == [0, 0, 0]:
    break
  tri.sort()
  if tri[0]**2 + tri[1]**2 == tri[2]**2:
    print('right')
  else:
    print("wrong")
