# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.
# # class 4
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    distance = [sys.maxsize] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)

        if distance[now] >= now_dist:
            for next, cost in graph[now]:
                next_dist = now_dist + cost

                if distance[next] > next_dist:
                    distance[next] = next_dist
                    heapq.heappush(queue, (next_dist, next))

    return distance


if __name__ == "__main__":
    n, e = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        a, b, c = map(int, input().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().strip().split())
    dist_1 = dijkstra(1)
    dist_v1 = dijkstra(v1)
    dist_v2 = dijkstra(v2)
    dist_1_v1_v2_n = dist_1[v1] + dist_v1[v2] + dist_v2[n]
    dist_1_v2_v1_n = dist_1[v2] + dist_v2[v1] + dist_v1[n]
    ans = min(dist_1_v1_v2_n, dist_1_v2_v1_n)
    print(ans if ans < sys.maxsize else -1)
