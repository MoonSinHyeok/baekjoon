l = []
while True:
    a, b = map(int, input().split())
    if(a==0 and b==0):
        break
    l.append(a+b)

for i in range(len(l)):
    print(l[i])
