T = int(input())
for i in range(T):
  n, s, d = map(int, input().split())
  sum = 0
  for _ in range(n):
    di, vi = map(int, input().split())
    if di / s <= d:
      sum += vi
  print(f"Data Set {i+1}:\n{sum}\n")
