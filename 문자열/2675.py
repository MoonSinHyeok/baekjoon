T = int(input())

result = []

for i in range(T):
    n, s = input().split()
    _ = ""
    for j in s:
        _ += j*int(n)
    result.append(_)

for i in range(T):
    print(result[i])
