# 트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.
# # class 4
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [-1 for _ in range(v+1)]
    queue = deque([start])
    visited[start] = 0
    max_data = [0, 0]
    while queue:
        node = queue.popleft()
        for next_node, distance in graph[node]:
            if visited[next_node] == -1:
                next_distance = distance + visited[node]
                visited[next_node] = next_distance
                queue.append(next_node)
                if max_data[1] < next_distance:
                    max_data = next_node, next_distance
    return max_data


if __name__ == "__main__":
    v = int(input())

    graph = [[] for _ in range(v+1)]
    for _ in range(v-1):
        node, root, cost = map(int, input().strip().split())
        graph[node].append((root, cost))
        graph[root].append((node, cost))

    node, distance = bfs(1)
    node, distance = bfs(node)
    print(distance)
