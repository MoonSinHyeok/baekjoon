import sys

input = sys.stdin.readline

line = input()
line_minus = list(line.split("-"))
result = 0

for i in range(len(line_minus)):
  part = list(map(int, line_minus[i].split("+")))
  if i == 0:
    result += sum(part)
  else:
    result -= sum(part)

print(result)
