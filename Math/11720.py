import sys

input = sys.stdin.readline

n = int(input())

nums = list(input())
result = 0
for i in nums:
  try:
    result += int(i)
  except Exception:
    continue
print(result)
