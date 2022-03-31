N = int(input())

ans = []
for i in range(N):
    a = list(map(str, input().split("X")))
    l = [itm for itm in a if itm != '']
    _ = 0
    for j in range(len(l)):
        result = [k+1 for k in range(len(l[j]))]
        _ += sum(result)
    ans.append(_)

for i in range(N):
    print(ans[i])
