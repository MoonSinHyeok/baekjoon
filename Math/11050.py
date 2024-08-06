N, K = map(int, input().split())


# (n, k) = (n-1, k) + (n-1, k-1)
def bino_coef(n, k):
  if k == 0 or n == k:
    return 1
  return bino_coef(n - 1, k) + bino_coef(n - 1, k - 1)


print(bino_coef(N, K))
