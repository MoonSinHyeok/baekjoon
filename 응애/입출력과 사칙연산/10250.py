T = int(input())

H, W, N = 1, 1, 1
for _ in range(T):
  H, W, N = map(int, input().split())

  floor = N % H if N % H != 0 else H
  ho = N // H + 1 if N % H != 0 else N // H
  print(floor * 100 + ho)
