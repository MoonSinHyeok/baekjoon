n, x = map(int, input().split())

l = list(map(int, input().split()))
ll = []

for i in range(n):
    if(l[i]<x):
        ll.append(l[i])

for i in range(len(ll)):
    print(ll[i], end=" ")
