# heap = [0]
# N = int(input())

# def min_heapify(arr, idx):
#   left = 2 * idx
#   right = 2 * idx + 1
#   smallest = idx
#   if left <= len(arr)-1 and arr[left] < arr[smallest]:
#     smallest = left
#   if right <= len(arr)-1 and arr[right] < arr[smallest] and arr[right] < arr[left]:
#     smallest = right
#   if smallest != idx:
#     arr[idx], arr[smallest] = arr[smallest], arr[idx]
#     min_heapify(arr, smallest)

# def pop_min(arr):
#   if len(arr) <= 1:
#     return 0
#   min_val = arr[1]
#   # print(arr)
#   last = arr.pop()
#   try:
#     arr[1] = last
#   except Exception:
#     return min_val
#   min_heapify(arr, 1)
#   return min_val
  
# for _ in range(N):
#   x = int(input())
#   if x == 0:
#     if len(heap) <= 1:
#       print(0)
#     else:
#       print(pop_min(heap))
#   else:
#     heap.insert(1, x)
#     min_heapify(heap, 1)

import heapq
import sys

input = sys.stdin.readline

q = []
N = int(input())

for _ in range(N):
  x = int(input())
  if (x == 0):
    if len(q) == 0:
      print(0)
    else:
      print(heapq.heappop(q))
  else:
    heapq.heappush(q, x)