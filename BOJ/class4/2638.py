# 치즈

# # class 4
import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, m, graph):
    global ans
    visited = [[True for _ in range(m)] for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    have_cheeze = False

    queue = deque([(0, 0)])
    visited[0][0] = False
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx, ny = x+dx[direction], y+dy[direction]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = False
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0

            if graph[i][j] == 2:
                graph[i][j] = 1

            if not have_cheeze:
                if graph[i][j] == 1:
                    have_cheeze = True

    ans += 1
    if have_cheeze:
        bfs(n, m, graph)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]
    ans = 0

    bfs(n, m, graph)
    print(ans)
