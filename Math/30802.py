N = int(input())

Tshirt = list(map(int, input().split()))

T, P = map(int, input().split())

# size / T + 1 if (size % T) else 0
sumT = 0
for size in Tshirt:
  sumT += size // T + int(size % T != 0)

print(sumT)
print(N // P, N % P)
