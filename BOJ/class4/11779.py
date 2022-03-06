# n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.

# class 4++

import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(start, end, graph):
    distance = [sys.maxsize for _ in range(city_num+1)]
    visited = [0 for _ in range(city_num+1)]

    queue = []
    distance[start] = 0
    heappush(queue, (0, start))
    while queue:
        now_dist, now = heappop(queue)
        if now_dist <= distance[now]:
            for next, cost in graph[now]:
                next_dist = now_dist + cost
                if next_dist < distance[next]:
                    visited[next] = now
                    distance[next] = next_dist
                    heappush(queue, (next_dist, next))

    count = 1
    node = [end]
    while True:
        count += 1
        node.insert(0, visited[node[0]])
        if node[0] == start:
            break

    print(distance[end])
    print(count)
    print(*node)


if __name__ == "__main__":
    city_num = int(input())
    bus_num = int(input())

    graph = [[] for _ in range(city_num+1)]
    for _ in range(bus_num):
        start, end, cost = map(int, input().strip().split())
        graph[start].append((end, cost))

    start, end = map(int, input().strip().split())

    dijkstra(start, end, graph)
