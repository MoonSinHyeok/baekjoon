import sys

input = sys.stdin.readline
N = int(input())

# li = []
# for _ in range(N):
#   li.append(int(input()))

# def merge(left, right):
#   sorted_li = []
#   i, j = 0, 0
#   while i < len(left) and j < len(right):
#     if left[i] < right[j]:
#       sorted_li.append(left[i])
#       i += 1
#     else:
#       sorted_li.append(right[j])
#       j += 1
#   if i >= len(left):
#     sorted_li += right[j:]
#   else:
#     sorted_li += left[i:]
#   return sorted_li

# def merge_sort(li):
#   if len(li) <= 1:
#     return li

#   mid = len(li) // 2
#   left = merge_sort(li[:mid])
#   right = merge_sort(li[mid:])
#   return merge(left, right)

# sorted_li = merge_sort(li)

# for e in sorted_li:
#   print(e)

li_plus = [0] * 1000001
li_minus = [0] * 1000001

for _ in range(N):
  insert = int(input())
  if insert >= 0:
    li_plus[insert] = 1
  else:
    li_minus[-1 * insert] = 1

for i in range(1000000, 0, -1):
  if li_minus[i]:
    print(-1 * i)

for i in range(1000001):
  if li_plus[i]:
    print(i)
