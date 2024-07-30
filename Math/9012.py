T = int(input())
for _ in range(T):
  s = input()
  a, b = 0, 0
  check = False
  for e in s:
    if e == "(":
      a += 1
    else:
      if a > 0:
        a -= 1
      else:
        print("NO")
        check = True
        break

  if check:
    continue
  if a == 0 and b == 0:
    print("YES")
  else:
    print("NO")
