N = int(input())
r = []

for i in range(N):
    l = list(map(int, input().split()))
    average = sum(l[1:])/l[0]
    ll = [item for item in l[1:] if item > average]
    k = len(ll)/l[0]*100
    r.append(k)

for i in range(N):
    print(format(r[i], ".3f"), end="")
    print("%")
