import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # 수열
answer = [-1] * N  # 기본값을 오큰수가 존재하지 않는경우인 -1로 설정
stack = []  # 스택

for i in range(N):
  while stack and A[
      stack[-1]] < A[i]:  # 스택이 비어있지 않고 수열의 다음 수가 스택의 최상단 수보다 클 경우
    answer[stack.pop()] = A[i]  # pop된 수의 인덱스에 수열의 다음 수 저장
  stack.append(i)  # 수열의 다음 수 스택에 넣기

for i in answer:
  print(i, end=" ")
