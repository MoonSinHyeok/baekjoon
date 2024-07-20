import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pocketmon = {0: "unknown"}

for i in range(1, N + 1):
  pocketmon[i] = input().replace("\n", "")

pocketmon_r = {v: k for k, v in pocketmon.items()}

result = []

for _ in range(M):
  question = input().replace("\n", "")
  try:
    num = int(question)
    result.append(pocketmon[num])
  except Exception:
    name = question
    result.append(pocketmon_r[name])

for ans in result:
  print(ans)
