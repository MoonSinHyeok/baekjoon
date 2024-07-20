import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(r, c, m):
  global max

  visited[ord(board[r][c]) - 65] = 1
  m += 1
  if max < m:
    max = m

  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]
  for i in range(4):
    pr = r + dr[i]
    pc = c + dc[i]
    if 0 <= pr < R and 0 <= pc < C and not visited[ord(board[pr][pc]) - 65]:
      dfs(pr, pc, m)
      visited[ord(board[pr][pc]) - 65] = 0


R, C = map(int, input().split())
board = []
for _ in range(R):
  board.append(list(input().rstrip()))

visited = [0 for _ in range(26)]  # 알파벳
max = 0

dfs(0, 0, 0)
print(max)
