import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

print(min(l), max(l))
