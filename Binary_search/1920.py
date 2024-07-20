import sys

input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))

M = int(input())
m = list(map(int, input().split()))

n.sort()


def find(arr, len, key):
  l = 0
  r = len - 1

  while l <= r:
    mid = (l + r) // 2

    if arr[mid] == key:
      return True
    elif arr[mid] > key:
      r = mid - 1
    else:
      l = mid + 1
  return False


for i in m:
  if find(n, N, i):
    print(1)
  else:
    print(0)
