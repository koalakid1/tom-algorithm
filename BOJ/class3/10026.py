# 적록색약
# class3++
import sys
from collections import deque
input = sys.stdin.readline


def dfs(n, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[True for _ in range(n)] for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                visited[i][j] = False
                queue = deque([(i, j)])

                color = graph[i][j]
                while queue:
                    x, y = queue.popleft()
                    for direction in range(4):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if 0 <= nx < n and 0 <= ny < n:
                            if visited[nx][ny] and graph[nx][ny] == color:
                                visited[nx][ny] = False
                                queue.append((nx, ny))
                ans += 1

    return ans


if __name__ == "__main__":
    n = int(input())

    rgb_graph = []
    rb_graph = []
    for _ in range(n):
        rgb_line = input().strip()
        rb_line = ""
        for rgb in rgb_line:
            if rgb == "G":
                rb_line += "R"
            else:
                rb_line += rgb

        rgb_graph.append(rgb_line)
        rb_graph.append(rb_line)

    print(dfs(n, rgb_graph), end=" ")
    print(dfs(n, rb_graph))
