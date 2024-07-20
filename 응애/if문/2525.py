H, M = map(int, input().split())
C = int(input())

k = H*60 + M + C

print(k//60%24, end = " ")
print(k%60)
