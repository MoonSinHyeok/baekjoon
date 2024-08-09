N = int(input())
paper = []
for _ in range(N):
  paper.append(list(map(int, input().split())))

white = 0
blue = 0


def solution(paper, N):
  global white, blue
  check = paper[0][0]

  if N == 1:
    if check == 0:
      white += 1
    else:
      blue += 1
    return

  flag = True
  for i in range(N):
    if not flag:
      break
    for j in range(N):
      if paper[i][j] != check:
        flag = False
        break

  if flag:
    if check == 0:
      white += 1
    else:
      blue += 1
    return

  p1, p2, p3, p4 = [], [], [], []
  for i in range(N // 2):
    p1.append(paper[:N // 2][i][:N // 2])
    p2.append(paper[:N // 2][i][N // 2:])
    p3.append(paper[N // 2:][i][:N // 2])
    p4.append(paper[N // 2:][i][N // 2:])
  solution(p1, N // 2)
  solution(p2, N // 2)
  solution(p3, N // 2)
  solution(p4, N // 2)


solution(paper, N)

print(white)
print(blue)
