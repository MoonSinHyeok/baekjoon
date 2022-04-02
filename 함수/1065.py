def a(N):
    ans = 0
    if(len(str(N)) == 1 or len(str(N)) == 2):
        for i in range(1, N+1):
            ans += 1
    elif(len(str(N)) == 3):
        ans = 99
        for i in range(100, N+1):
            k = str(i)
            if(int(k[0])-int(k[1]) == int(k[1])-int(k[2])):
                ans += 1
    elif(len(str(N)) == 4):
        ans = 144
        for i in range(1000, N+1):
            k = str(i)
            if(int(k[0])-int(k[1]) == int(k[1])-int(k[2]) and int(k[1])-int(k[2]) == int(k[2])-int(k[3]) and int(k[0])-int(k[1]) == int(k[2])-int(k[3])):
                ans += 1
    
    return ans

N = int(input())
print(a(N))
