import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    graph = []
    
    minsick_x = -1
    minsick_y = -1
    location_x = []
    door = 0
    for j in range(m):
        line = input().strip()
        find_minsick = line.find('0')
        for i in range(n):
            if line[i] >= 'A' and line[i] <= 'F':
                door |= 1 << (ord(line[i]) - ord('A')) 

        if find_minsick != -1:
            minsick_y = j
            minsick_x = find_minsick
        
        graph.append(line)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    d = [[[True for _ in range(1 << 6)] for _ in range(n)] for _ in range(m)]

    answer = -1
    q = deque([(minsick_x, minsick_y, 0, 0)])
    while q:
        x, y, status, distance = q.popleft()
        if answer == -1 or distance < answer:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if d[ny][nx][status]:
                        n_distance = distance + 1
                        if graph[ny][nx] != "#":
                            if graph[ny][nx] == "1":
                                answer = n_distance
                            
                            elif graph[ny][nx] >= "a" and graph[ny][nx] <= "f":
                                n_status = status | (1 << ord(graph[ny][nx]) - ord('a'))
                                d[ny][nx][status] = False
                                q.append((nx, ny, n_status, n_distance))
                                
                            elif graph[ny][nx] >= "A" and graph[ny][nx] <= "F":
                                location = ord(graph[ny][nx]) - ord("A")
                                check = (door & status) & (1 << location)
                                if check:
                                    d[ny][nx][status] = False
                                    q.append((nx, ny, status, n_distance))
                            
                            else:
                                d[ny][nx][status] = False
                                q.append((nx, ny, status, n_distance))
                                
                        
    print(answer)