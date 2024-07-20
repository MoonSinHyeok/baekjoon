import sys

input = sys.stdin.readline

S, P = map(int, input().split())
str = input()
A, C, G, T = list(map(int, input().split()))
check = [0, 0, 0, 0]  # 0: A, 1: C, 2: G, 3: T
cnt = 0

for i in range(P):
  if str[i] == 'A':
    check[0] += 1
  elif str[i] == 'C':
    check[1] += 1
  elif str[i] == 'G':
    check[2] += 1
  else:
    check[3] += 1

if (check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T):
  cnt += 1

end = P - 1
for i in range(S - P):
  if str[i] == 'A':
    check[0] -= 1
  elif str[i] == 'C':
    check[1] -= 1
  elif str[i] == 'G':
    check[2] -= 1
  else:
    check[3] -= 1

  if str[end + 1] == 'A':
    check[0] += 1
  elif str[end + 1] == 'C':
    check[1] += 1
  elif str[end + 1] == 'G':
    check[2] += 1
  else:
    check[3] += 1

  if (check[0] >= A and check[1] >= C and check[2] >= G and check[3] >= T):
    cnt += 1

  i += 1
  end += 1

print(cnt)
