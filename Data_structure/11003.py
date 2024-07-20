# import sys
# from collections import deque

# input = sys.stdin.readline

# N, L = map(int, input().split())
# A = list(map(int, input().split()))
# d = deque()

# # print(N, L)
# for i in range(N):
#   while d and d[-1][0] > A[i]:
#     # print(d)
#     d.pop()
#   d.append((A[i], i))
#   if d[0][1] <= i - L:
#     d.popleft()
#   print(d[0][0], end=' ')

