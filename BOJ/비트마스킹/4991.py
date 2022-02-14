import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    while True:  
        n, m = map(int, input().strip().split())
        if n == m == 0:
            break
        
        ox = -1
        oy = -1
        graph = [] 
        location_dirty = []
        for j in range(m):
            line = input().strip()
            find_o = line.find('o')
            for i in range(n):
                if line[i] == '*':
                    location_dirty.append((i,j))
            
            if find_o != -1:
                sy = j
                sx = find_o
            
            graph.append(line)

        num_dirty = len(location_dirty)
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        d = [[[True for _ in range(1 << num_dirty)] for _ in range(n)] for _ in range(m)]

        answer = -1
        q = deque([(sx, sy, 0, 0)])
        while q:
            x, y, status, distance = q.popleft()
            if answer == -1 or distance < answer:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and d[ny][nx][status]:
                        d[ny][nx][status] = False
                        n_distance = distance + 1
                        if graph[ny][nx] != "x":
                            if graph[ny][nx] == "*":
                                rank_x = location_dirty.index((nx, ny))
                                n_status = status | (1 << rank_x)
                                if n_status + 1 == 1 << num_dirty:
                                    answer = n_distance
                                q.append((nx, ny, n_status, n_distance))
                            else:
                                q.append((nx, ny, status, n_distance))
        print(answer)