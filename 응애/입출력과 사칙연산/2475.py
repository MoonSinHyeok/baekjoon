import sys

input = sys.stdin.readline

nums = list(map(int, input().rstrip("\n").split()))

sum = 0
for n in nums:
  sum += n**2

print(sum % 10)
