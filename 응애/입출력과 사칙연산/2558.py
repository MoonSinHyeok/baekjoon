a = int(input())
b = input()
leng = len(b)

for i in range(leng):
    print(a*int(b[leng-i-1]))

print(a*int(b))
