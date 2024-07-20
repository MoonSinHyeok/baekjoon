num = int(input())

n = num
count = 0

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = b*10 + c
    count += 1

    if(n == num):
        break

print(count)
