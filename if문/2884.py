H, M = map(int, input().split())

a = M - 45

if(a>=0):
    print(H, end = " ")
    print(a)
else:
    if(H==0):
        print(23, end = " ")
        print(60+a)
    else:
        print(H-1, end = " ")
        print(60+a)
