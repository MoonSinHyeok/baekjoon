# 백준 14938. 서강그라운드

# 1) 지역의 개수n 수색범위m 길의 개수r 입력
# 2) n개의 숫자로 각 지역의 아이템 수 입력 -> n 크기의 리스트 하나 만들고 저장
# 3) r개의 줄에 각 지역에 연결된 지역 거리 입력됨 -> n * n 크기의 그래프를 만들고 저장. 연결되어 있지 않은 지역의 값은 maxsize로 설정
# 4) dfs로 시작지점에서 수색범위 내의 지역들을 탐색 -> 범위 내의 노드 정보를 리턴
# 5) 아이템 개수 총합이 ans보다 클 경우 ans 갱신
# 6) 4, 5 과정을 모든 지역에 대해 반복?

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

item = list(map(int, input().split()))
graph = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):
  graph[i][i] = 0

for i in range(r):
  a, b, dist = map(int, input().split())
  graph[a - 1][b - 1] = dist
  graph[b - 1][a - 1] = dist


def dijkstra(start):
  global m
  dist = [sys.maxsize] * n
  dist[start] = 0
  q = []
  heappush(q, (start, 0))
  while q:
    now, cost = heappop(q)
    for i in range(n):
      tmp = graph[now][i] + cost
      if tmp < dist[i] and tmp <= m:
        dist[i] = tmp
        heappush(q, (i, tmp))
  result = []
  for i in range(n):
    if dist[i] != sys.maxsize:
      result.append(i)
  return result


ans = 0
for i in range(n):
  temp = dijkstra(i)
  tmp = 0
  for e in temp:
    tmp += item[e]
  ans = max(ans, tmp)

print(ans)
