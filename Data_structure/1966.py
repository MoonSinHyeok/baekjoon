import sys
from collections import deque

input = sys.stdin.readline
T = int(input())  # 테스트 케이스

for _ in range(T):
  N, P = map(int, input().split())  # 문서의 개수와, 몇번째 인쇄인지 궁금한 문서의 인덱스
  d = deque(map(int, input().split()))  # 문서의 중요도

  cnt = 1  # 인쇄한 문서의 개수
  while d:
    if d[0] < max(d):
      d.append(d.popleft())
    else:
      if P == 0:
        break
      else:
        d.popleft()
        cnt += 1
    P = P - 1 if P > 0 else len(
        d) - 1  # 중요도가 더 높은 문서가 있다면 다시 맨뒤로 가기 때문에 len(d) - 1로 설정
  print(cnt)
