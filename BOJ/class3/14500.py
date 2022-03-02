# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 한다.

# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.
# class3++
import sys
input = sys.stdin.readline


def dfs(x, y, depth, value):
    global max_value
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if depth == 4:
        max_value = max(max_value, value)
    else:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:

                    next_value = value + graph[nx][ny]
                    if depth == 2:
                        visited[nx][ny] = 1
                        dfs(x, y, depth+1, next_value)
                        visited[nx][ny] = 0

                    visited[nx][ny] = 1
                    dfs(nx, ny, depth+1, next_value)
                    visited[nx][ny] = 0


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    max_value = 0
    for x in range(n):
        for y in range(m):
            visited[x][y] = 1
            dfs(x, y, 1, graph[x][y])
            visited[x][y] = 0
    print(max_value)
