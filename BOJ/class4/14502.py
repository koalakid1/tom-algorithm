# 연구소

# # class 4+
from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def graph_check(new_wall, graph):
    for x, y in new_wall:
        if graph[x][y] != 0:
            return False
    return True


def bfs(new_wall, graph):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for x, y in new_wall:
        graph[x][y] = 1

    virus_num = 0
    visited = [[True for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 and visited[i][j]:
                virus_num += 1
                visited[i][j] = False
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for direction in range(4):
                        nx, ny = x+dx[direction], y+dy[direction]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and graph[nx][ny] != 1:
                            graph[nx][ny] = 2
                            virus_num += 1
                            visited[nx][ny] = False
                            queue.append((nx, ny))

    return safety_zone - virus_num


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    new_walls = [(i, j) for i in range(n) for j in range(m)]
    new_walls = combinations(new_walls, 3)
    safety_zone = n * m - 3
    graph = []
    for _ in range(n):
        line = list(map(int, input().strip().split()))
        for type in line:
            if type == 1:
                safety_zone -= 1
        graph.append(line)

    ans = 0
    for new_wall in new_walls:
        if graph_check(new_wall, graph):
            safety = bfs(new_wall, deepcopy(graph))
            if safety > ans:
                ans = safety
    print(ans)
