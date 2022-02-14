import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    graph = []
    
    sx = -1
    sy = -1
    location_x = []
    for j in range(m):
        line = input().strip()
        find_s = line.find('S')
        for i in range(n):
            if line[i] == 'X':
                location_x.append((i,j))
        
        if find_s != -1:
            sy = j
            sx = find_s
        
        graph.append(line)

    num_x = len(location_x)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    d = [[[True for _ in range(1 << num_x)] for _ in range(n)] for _ in range(m)]

    answer = sys.maxsize
    q = deque([(sx, sy, 0, 0)])
    while q:
        x, y, status, distance = q.popleft()
        if distance < answer:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and d[ny][nx][status]:
                    d[ny][nx][status] = False
                    n_distance = distance + 1
                    if graph[ny][nx] != "#":
                        if graph[ny][nx] == "E":
                            if status + 1 == 1 << num_x:
                                answer = min(distance+1, answer)
                        elif graph[ny][nx] == "X":
                            rank_x = location_x.index((nx, ny))
                            n_status = status | (1 << rank_x)
                            q.append((nx, ny, n_status, n_distance))
                        else:
                            q.append((nx, ny, status, n_distance))
    print(answer)