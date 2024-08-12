A, B, C = map(int, input().split())
# A의 B제곱, C로 나누기
# 거듭제곱 분할정복:
# A^C = A^(C/2) * A^(C/2)[C = 짝수]
# A^C = A^((C-1)/2) * A^((C-1)/2) * A[C = 홀수]


def sol(A, B, C):
  if B == 1:
    return A % C
  else:
    tmp = sol(A, B // 2, C)
    if B % 2:
      return tmp * tmp * A % C
    else:
      return tmp * tmp % C


print(sol(A, B, C))

# tmp = 1
# save = []
# flag = False
# index = None

# for _ in range(B):
#   tmp = tmp * A % C
#   if tmp not in save:
#     save.append(tmp)
#   else:
#     index = save.index(tmp)
#     flag = True
#     break
# else:
#   print(tmp)

# rule = save[index:]

# if flag:
#   print(rule[B % len(rule) - 1])
