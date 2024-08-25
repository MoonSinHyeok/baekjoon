N = int(input())

vertical_check = [False] * N
# 동일 세로선 상에 있는지 체크

down_cross_check = [False] * 2 * N
# 내려가는 대각 체크, x-y의 최대는 n-1 최소는 -n+1. 보정으로 n을 더해주기

up_cross_check = [False] * 2 * N
# 올라가는 대각 체크, x+y의 최대는 2n-2

ans = 0


def check(x, y):
  global vertical_check, down_cross_check, up_cross_check
  if vertical_check[x]:
    return False
  if down_cross_check[x - y + N]:
    return False
  if up_cross_check[x + y]:
    return False
  return True


def toggle(x, y):
  global vertical_check, down_cross_check, up_cross_check
  vertical_check[x] = not vertical_check[x]
  down_cross_check[x - y + N] = not down_cross_check[x - y + N]
  up_cross_check[x + y] = not up_cross_check[x + y]


def Nqueen(y):
  global ans
  if y == N:
    ans += 1
    return
  else:
    for i in range(N):
      if check(i, y):
        toggle(i, y)
        Nqueen(y + 1)
        toggle(i, y)


Nqueen(0)
print(ans)

# board = [[0] * N for _ in range(N)]

# ans = 0

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 0

# def check(x, y):
#   for i in range(x):
#     if board[i][y]:
#       return False
#   for i in range(1, x + 1):
#     if y - i >= 0 and board[x - i][y - i]:
#       return False
#     if y + i < N and board[x - i][y + i]:
#       return False
#   return True

# def Nqueen(x):
#   global ans, board
#   if x == N:
#     ans += 1
#     return
#   else:
#     for i in range(N):
#       if check(x, i):
#         board[x][i] = 1
#         Nqueen(x + 1)
#         board[x][i] = 0

# Nqueen(0)
# print(ans)
