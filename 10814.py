import sys

input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
  age, name = input().rstrip("\n").split()
  age = int(age)
  li.append((age, name))

li.sort(key=lambda x: x[0])
for e in li:
  print(e[0], e[1])
