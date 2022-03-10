# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 두 칸이 변을 공유할 때, 인접하다고 한다.

# 각각의 벽에 대해서 다음을 구해보려고 한다.

# 벽을 부수고 이동할 수 있는 곳으로 변경한다.
# 그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# class 5
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[True for _ in range(m)] for _ in range(n)]
    
    group_idx = 1
    
    for i in range(n):
        for j in range(m):
            if not graph[i][j] and visited[i][j]:
                queue = deque([(i,j)])
                visited[i][j] = False
                group_graph[i][j] = group_idx
                count = 1
                while queue:
                    x,y = queue.popleft()
                    for direct in range(4):
                        nx = x + dx[direct]
                        ny = y + dy[direct]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and not graph[nx][ny]:
                            visited[nx][ny] = False
                            group_graph[nx][ny] = group_idx
                            count += 1
                            queue.append((nx, ny))
                            
                group[group_idx] = count % 10
                group_idx += 1

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    graph = [list(map(int, input().strip())) for _ in range(n)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    
    group_graph = [[0 for _ in range(m)] for _ in range(n)]
    group = {}
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                group_set = set()
                for direct in range(4):
                        nx = i + dx[direct]
                        ny = j + dy[direct]
                        if 0 <= nx < n and 0 <= ny < m and group_graph[nx][ny]:
                            group_set.add(group_graph[nx][ny])
                for idx in group_set:
                    graph[i][j] += group[idx]
                graph[i][j] %= 10
        print("".join(map(str,graph[i])))