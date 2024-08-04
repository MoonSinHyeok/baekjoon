import sys

input = sys.stdin.readline

A = sum(map(int, input().rstrip("\n").split()))
B = sum(map(int, input().rstrip("\n").split()))
print(A if A >= B else B)
