li = list(map(int, input().split()))
li.sort()

gap = (li[1] - li[0]) if (li[1] - li[0] < li[2] - li[1]) else (li[2] - li[1])

if li[-1] + gap <= 100:
  for i in range(3):
    if li[i] + gap not in li:
      print(li[i] + gap)
      break
else:
  for i in range(2, -1, -1):
    if li[i] - gap not in li:
      print(li[i] - gap)
      break
