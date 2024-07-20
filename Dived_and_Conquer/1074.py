import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())


def z(N, r, c):
  if N == 0:
    if r > 2**N and c > 2**N:
      return 3
    elif r > 2**N and c <= 2**N:
      return 2
    elif r <= 2**N**2 and c > 2**N:
      return 1
    else:
      return 0

  if r > 2**N and c > 2**N:
    return (2**N)**2 * 3 + z(N - 1, r - 2**N, c - 2**N)
  elif r > 2**N and c <= 2**N:
    return (2**N)**2 * 2 + z(N - 1, r - 2**N, c)
  elif r <= 2**N**2 and c > 2**N:
    return (2**N)**2 + z(N - 1, r, c - 2**N)
  else:
    return z(N - 1, r, c)


# 입력 행 열의 값은 0부터 (2**N)-1까지 이므로 1~2**N으로 수정
print(z(N - 1, r + 1, c + 1))
