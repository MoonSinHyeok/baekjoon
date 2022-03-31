import sys

N = int(input())

l = list(map(int, sys.stdin.readline().split()))
m = max(l)

print(sum(l)*100/m/N)
