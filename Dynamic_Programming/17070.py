import sys

input = sys.stdin.readline

N = int(input())

house = []
for _ in range(N):
  house.append(list(map(int, input().rstrip().split())))

# 파이프 첫 위치 (1,1) (1,2) => (0, 0) (0, 1) y, x좌표
# dp
# 파이프가 대각상태인 경우, 가로상태인 경우, 세로상태인
# 경우 나눠서 다음 위치에 += 1?

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# 각 칸마다 가로, 세로, 대각선 파이프가 올 수 있는 경우 저장

for i in range(1, N):
  if house[0][i] != 1:
    dp[0][i][0] = 1  # 첫째 줄 가로 파이프 채우기
  else:
    break

for y in range(1, N):
  for x in range(1, N):
    # 대각
    if house[y][x] != 1 and house[y][x - 1] != 1 and house[y - 1][x] != 1:
      dp[y][x][2] = dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x -
                                                                          1][2]

    # 가로 세로
    if house[y][x] != 1:
      dp[y][x][0] = dp[y][x - 1][0] + dp[y][x - 1][2]
      dp[y][x][1] = dp[y - 1][x][1] + dp[y - 1][x][2]

sum = 0
for pipe in dp[N - 1][N - 1]:
  sum += pipe

print(sum)
