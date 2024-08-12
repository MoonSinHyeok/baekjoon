import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().rstrip("\n").split()))

X_set = set(X)
X_set = sorted(list(X_set))

dict = {X_set[i]: i for i in range(len(X_set))}

for e in X:
  print(dict[e], end=" ")
