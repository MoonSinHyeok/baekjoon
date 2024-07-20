import sys

input = sys.stdin.readline

N = int(input())  # 재료의 개수
nums = list(map(int, input().split()))

nums.sort()
cnt = 0

for i in range(N):
  target = nums[i]
  left = 0
  right = N - 1
  while left < right:
    if nums[left] + nums[right] < target:
      left += 1
    elif nums[left] + nums[right] > target:
      right -= 1
    else:
      if left != i and right != i:
        cnt += 1
        break
      elif left == i:
        left += 1
      elif right == i:
        right -= 1

print(cnt)
