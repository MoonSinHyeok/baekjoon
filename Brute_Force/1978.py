import sys

input = sys.stdin.readline

N = input()
line = list(map(int, input().rstrip("\n").split()))

check = [1] * 1001

for i in range(2, 1001):
  if check[i]:
    for j in range(i * 2, 1001, i):
      check[j] = 0

sum = 0
for e in line:
  if e > 1 and check[e]:
    sum += 1

print(sum)
