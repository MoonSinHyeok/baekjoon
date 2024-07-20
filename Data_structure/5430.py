T = int(input())

for _ in range(T):
  p = input()
  n = int(input())
  arr = input().strip("[]").split(",")
  if n == 0:
    arr = []

  reverse = False
  for order in p:
    if order == "R":
      reverse = not reverse
    elif order == "D":
      if len(arr) > 0:
        if reverse:
          arr.pop()
        else:
          arr.pop(0)
      else:
        print("error")
        break
  else:
    if reverse:
      print("[" + ",".join(arr[::-1]) + "]")
    else:
      print("[" + ",".join(arr[:]) + "]")
