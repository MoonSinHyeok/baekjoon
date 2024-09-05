n = int(input())

# tmp1 = 0
# tmp2 = 1

# if n == 0:
#   print(0)
# elif n == 1:
#   print(1)
# else:
#   for i in range(2, n + 1):
#     tmp = tmp2
#     tmp2 = (tmp1 + tmp2) % 1000000007
#     tmp1 = tmp
#   print(tmp2)

# Fn = Fn-1 + Fn-2 = Fn-2 + Fn-3 + Fn-2 = 2 * Fn-2 + Fn-3
# = 2 * (Fn-3 + Fn-4) + Fn-3 = 3 * Fn-3 + 2 * Fn-4
# Fn -> Fn-1 + Fn-2 -> 2 * Fn-2 + Fn-3 -> 3 * Fn-3 + 2 * Fn-4 ...

# def divide_and_conquer(a, b, n):
#   if n == 2:
#     return (a, b)
#   else:
#     return divide_and_conquer((a + b) % 1000000007, a, n - 1)

# n = n-1 n-2 = n-2 n-3 n-3 n-4 = n-3 n-4 n-4 n-5 n-4 n-5 n-5 n-6

# 행렬의 거듭제곱으로 풀라네? 젠장


def multiply(A, B):
  AB = [[0] * 2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        AB[i][j] += A[i][k] * B[k][j] % 1000000007
  return AB


def power(A, n):
  if n == 1:
    return A
  elif n % 2 == 0:
    return power(multiply(A, A), n // 2)
  else:
    return multiply(A, power(multiply(A, A), (n - 1) // 2))


fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

if n <= 17:
  print(fibo[n])
else:
  arr = [[1, 1], [1, 0]]
  arr2 = power(arr, n)
  print(arr2[0][1] % 1000000007)
