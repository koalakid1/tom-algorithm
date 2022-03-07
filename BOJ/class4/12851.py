# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# # class 4+
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, end):
    distance = [sys.maxsize] * 100001
    visited = [0] * 100001
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    visited[start] = 1
    count = 0
    while queue:
        now_dist, now = heapq.heappop(queue)

        if distance[now] >= now_dist:
            for next in [now-1, now+1, now*2]:
                if 0 <= next < 100001:
                    next_dist = now_dist + 1
                    if next_dist < distance[next]:
                        visited[next] = visited[now]
                        distance[next] = next_dist
                        heapq.heappush(queue, (next_dist, next))
                    elif next_dist == distance[next]:
                        visited[next] += visited[now]

    return [distance, visited]


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    distance, visited = dijkstra(n, k)
    print(f"{distance[k]}\n{visited[k]}")
