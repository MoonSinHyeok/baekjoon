import sys
n = []
for line in sys.stdin:
    n.append(int(line))

k = max(n)
print(k)
print(n.index(k)+1)
