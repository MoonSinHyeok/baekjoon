l = []

while True:
    try:
        A, B = map(int, input().split())
        l.append(A+B)
    except EOFError:
        break


for i in range(len(l)):
    print(l[i])
