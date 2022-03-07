# 미세먼지 안녕!

# # class 4+
import sys
input = sys.stdin.readline


def spread(r, c, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    spread_graph = [[0 for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                spread_value = graph[x][y] // 5
                remain_value = graph[x][y]
                for direction in range(4):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        spread_graph[nx][ny] += spread_value
                        remain_value -= spread_value
                spread_graph[x][y] += remain_value
            elif graph[x][y] == -1:
                spread_graph[x][y] = -1
    return spread_graph


def air_up_clean(r, c, graph, air):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    x = air
    y = 1
    temp = 0
    while True:
        if direction == 3 and x == air:
            break
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < r and 0 <= ny < c:
            temp, graph[x][y] = graph[x][y], temp
            x = nx
            y = ny
        else:
            direction += 1


def air_down_clean(r, c, graph, air):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    x = air
    y = 1
    temp = 0
    while True:
        if direction == 3 and x == air:
            break
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < r and 0 <= ny < c:
            temp, graph[x][y] = graph[x][y], temp
            x = nx
            y = ny
        else:
            direction += 1


def air_clean(r, c, graph, air_up, air_down):
    air_up_clean(r, c, graph, air_up)
    air_down_clean(r, c, graph, air_down)


def clean(r, c, t, air_up, air_down, graph):

    for _ in range(t):
        graph = spread(r, c, graph)
        air_clean(r, c, graph, air_up, air_down)
    return sum(sum(line) for line in graph) + 2


if __name__ == "__main__":
    r, c, t = map(int, input().strip().split())
    air_check = True
    air_up = -1
    air_down = -1
    graph = []
    for i in range(r):
        line = list(map(int, input().strip().split()))
        graph.append(line)
        if air_check:
            if line[0] == -1:
                air_up = i
                air_down = i+1
                air_check = False
    ans = clean(r, c, t, air_up, air_down, graph)
    print(ans)
