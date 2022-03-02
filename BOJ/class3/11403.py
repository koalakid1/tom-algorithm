# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
# class3++
import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, graph, start, end):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[True for _ in range(n)] for _ in range(n)]

    check = True
    queue = deque([start])
    while queue and check:
        now = queue.popleft()
        for next in graph[now]:
            if next == end:
                check = False
                break

            if visited[now][next]:
                visited[now][next] = False
                queue.append(next)

    return 0 if check else 1


if __name__ == "__main__":
    n = int(input())

    graph = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().strip().split()))
        for j in range(n):
            if line[j] == 1:
                graph[i].append(j)

    result_graph = [[] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            result_graph[x].append(bfs(n, graph, x, y))

    for line in result_graph:
        for data in line:
            print(data, end=" ")
        print()
