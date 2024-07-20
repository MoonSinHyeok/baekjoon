n = int(input())

l = []

for i in range(n):
    k = list(map(int, input().split()))
    l.append(k)

for i in range(n):
    print(f"Case #{i+1}: {l[i][0]} + {l[i][1]} =", l[i][0] + l[i][1])
