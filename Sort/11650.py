N = int(input())
li = []

for _ in range(N):
  li.append(list(map(int, input().split())))

li.sort(key=lambda x: (x[0], x[1]))
for e in li:
  print(*e)
