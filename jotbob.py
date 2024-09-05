li = []
for _ in range(3):
  li.append(input())

num = []
for i in range(3):
  if li[i] == "Fizz":
    pass
  elif li[i] == "Buzz":
    pass
  elif li[i] == "FizzBuzz":
    pass
  else:
    num.append((int(li[i]), i))

next = num[-1][0] + (3 - num[-1][1])
if next % 3 == 0 and next % 5 == 0:
  print("FizzBuzz")
elif next % 3 == 0:
  print("Fizz")
elif next % 5 == 0:
  print("Buzz")
else:
  print(next)
