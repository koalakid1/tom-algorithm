# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
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
    for _ in range(v):
        node_info = list(map(int, input().strip().split()))
        node = node_info[0]
        for idx in range(1, len(node_info) - 1, 2):
            graph[node].append((node_info[idx], node_info[idx+1]))
    node, distance = bfs(1)
    node, distance = bfs(node)
    print(distance)
