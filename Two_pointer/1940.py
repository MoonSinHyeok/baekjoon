import sys

input = sys.stdin.readline

N = int(input())  # 재료의 개수
M = int(input())  # 갑옷을 만드는데 필요한 수
materials = list(map(int, input().split()))  # 재료들의 고유 수

materials.sort()
start_index = 0
end_index = N - 1
cnt = 0

# 1 2 3 4 5 7
while start_index < end_index:
  if materials[start_index] + materials[end_index] == M:
    cnt += 1
    start_index += 1
    end_index -= 1
  elif materials[start_index] + materials[end_index] > M:
    end_index -= 1
  else:
    start_index += 1

print(cnt)
