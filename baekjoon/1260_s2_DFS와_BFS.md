## 내 솔루션
```python
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for g in graph:
    g.sort()

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        s = q.popleft()
        print(s, end=" ")
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)
```
dfs와 bfs를 동시에 요구하는 문제다. dfs와 bfs의 아주 기초적인 문제라고 할 수 있을 것 같다. 처음에 `정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고...` 
조건을 안 읽어서 graph를 정렬하는 부분이 없어서 연달아 틀렸다.. 문제를 잘 읽어보자.

## 문제 내용
### 문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

### 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

### 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.