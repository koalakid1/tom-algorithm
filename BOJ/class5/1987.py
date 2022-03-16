# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# class 5
import sys
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x, y, length):
    global ans
    ans = max(ans, length)
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < n and 0 <= ny < m:
            if visited_alpha[ord(graph[nx][ny]) - ord("A")]:
                if visited[nx][ny]:
                    visited[nx][ny] = False
                    visited_alpha[ord(graph[nx][ny]) - ord("A")] = False
                    dfs(nx, ny, length+1)
                    visited[nx][ny] = True
                    visited_alpha[ord(graph[nx][ny]) - ord("A")] = True


if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    graph = [input().strip() for _ in range(n)]
    visited = [[True for _ in range(m)] for _ in range(n)]
    visited_alpha = [True for _ in range(26)]
    visited[0][0] = False
    visited_alpha[ord(graph[0][0]) - ord("A")] = False

    ans = 1
    dfs(0, 0, 1)
    print(ans)
