"""

lgcpc A번 연습문제 MST 게임

N개의 정점과 M개의 양방향간선으로 이루어진 단순 그래프 G가 있다. 단순 그래프란, self-loop 간선(한 정점에서 자기 자신을 이어주는 간선)이 없고, 임의의 두 정점 사이 최대 한 개의 간선이 있는 그래프를 말한다. 단순 그래프의 스패닝 트리(Spanning Tree)는 다음 조건을 만족하는 간선의 집합이다.

    스패닝 트리를 구성하는 간선의 개수는 N-1개이다.
    그래프의 임의의 두 정점을 골랐을 때, 스패닝 트리에 속하는 간선만 이용해서 두 정점을 연결하는 경로를 구성할 수 있어야 한다.

스패닝 트리 중에서 간선의 가중치의 합이 최소인 것을 최소 스패닝 트리(Minimum Spanning Tree, MST)라고 부른다.

이제 그래프에서 MST 게임을 하려고 한다.

    MST 게임은 그래프에서 간선을 하나씩 제거하면서 MST의 비용을 구하는 게임이다. MST의 비용이란 MST를 이루고 있는 가중치의 합을 의미한다. 각 턴의 점수는 해당 턴에서 찾은 MST의 비용이 된다. 
    이 과정은 K턴에 걸쳐서 진행되며, 첫 턴에는 입력으로 주어진 그래프의 MST 비용을 구해야 한다.
    각 턴이 종료된 후에는 그 턴에서 구한 MST에서 가장 가중치가 작은 간선 하나를 제거한다.
    한 번 제거된 간선은 이후의 턴에서 사용할 수 없다.
    어떤 턴에서 MST를 만들 수 없다면, 그 턴의 점수는 0이다. 당연히 이후 모든 턴의 점수도 0점이다. 첫 턴에 MST를 만들 수 없는 경우도 있다.

양방향 간선으로 이루어진 단순 그래프와 K가 주어졌을 때, 각 턴의 점수가 몇 점인지 구하는 프로그램을 작성하시오.



***************************
입력

첫째 줄에 그래프 정점의 개수 N, 그래프 간선의 개수 M, 턴의 수 K가 주어진다. (2 ≤ N ≤ 1,000, 1 ≤ M ≤ min(10,000, N×(N-1)/2), 1 < K ≤ 100)

그 후 M개의 줄에 간선의 정보가 주어진다. 간선의 정보는 간선을 연결하는 두 정점의 번호 x, y로 이루어져 있다. 같은 간선이 여러 번 주어지는 경우는 없다. 간선의 가중치는 주어지는 순서대로 1, 2, ..., M이다.

정점의 번호는 1부터 N까지로 이루어져 있다.



*********************************8
출력

한 줄에 공백으로 구분하여 K개의 정수를 출력해야 한다. K개의 정수는 각 턴에 얻는 점수를 나타낸다. 




예제 입력 1

6 6 2
1 2
2 3
1 3
4 5
5 6
4 6

예제 출력 1

0 0

첫 턴에 MST를 찾을 수 없어서 모든 턴의 점수가 0이 된다.
예제 입력 2

6 7 3
2 4
1 2
4 6
1 3
2 3
4 5
5 6

예제 출력 2

16 0 0

예제 입력 3

4 5 4
3 4
1 3
1 4
1 2
2 4

예제 출력 3

7 9 0 0

예제 입력 4

5 7 4
1 2
2 3
3 4
4 5
1 5
1 4
1 3

예제 출력 4

10 14 0 0

예제 입력 5

6 9 6
1 2
2 3
3 4
4 5
5 6
1 6
1 4
2 5
3 6

예제 출력 5

15 20 26 32 35 0

나의 풀이: 프림 알고리즘

"""

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M, K = map(int, input().rstrip("\n").split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
  a, b = map(int, input().rstrip("\n").split())
  graph[a].append([i + 1, b])
  graph[b].append([i + 1, a])


def prim(start):
  queue = []
  heappush(queue, [0, start, start])

  visited = [False] * (N + 1)
  mst = []

  while queue:
    cost, node1, node2 = heappop(queue)

    if not visited[node2]:
      mst.append([cost, node1, node2])
    else:
      continue

    visited[node2] = True

    for c, n in graph[node2]:
      if not visited[n]:
        heappush(queue, [c, node2, n])
        ##### 디버그 용 #####
        # print("[-----queue_check-----]")
        # print(*queue, sep=' ')
        # print("----------------------")
        ###################
  if len(mst) == N:
    return sum(c for c, n1, n2 in mst), mst

  return 0, mst


for i in range(K):
  cost, mst = prim(1)
  ##### 디버그 용 #####
  # print(f"\n\n\ncase{i}:")
  # print("----graph----")
  # print(*(graph[1:]), sep=' ')
  # print("----mst----")
  # print(*mst, sep=' ')
  ###################

  if cost:
    print(cost, end=" ")
    mst.sort(key=lambda x: x[0])
    ##### 디버그 용 #####
    # print(f"\n*****{cost}*****\n")
    # print("----sorted_mst----")
    # print(*mst, sep=' ')
    ###################
    c, a, b = mst[1]
    for e in graph[a]:
      if e == [c, b]:
        graph[a].remove(e)
        break
    for e in graph[b]:
      if e == [c, a]:
        graph[b].remove(e)
        break

    ##### 디버그 용 #####
    # print("----graph_after----")
    # print(*(graph[1:]), sep=' ')
    ###################
  else:
    for _ in range(K - i):
      print(0, end=" ")
    break
