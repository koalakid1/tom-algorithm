# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# # class 4+
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, end):
    distance = [sys.maxsize] * (100001)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue and distance[end] == sys.maxsize:
        now_dist, now = heapq.heappop(queue)

        if distance[now] >= now_dist:
            minus_dist, minus = now_dist + 1, now - 1
            if 0 <= minus <= 100000:
                if distance[minus] > minus_dist:
                    distance[minus] = minus_dist
                    heapq.heappush(queue, (minus_dist, minus))

            plus_dist, plus = now_dist + 1, now + 1
            if 0 <= plus <= 100000:
                if distance[plus] > plus_dist:
                    distance[plus] = plus_dist
                    heapq.heappush(queue, (plus_dist, plus))

            teleport_dist, teleport = now_dist, now * 2
            if 0 <= teleport <= 100000:
                if distance[teleport] > teleport_dist:
                    distance[teleport] = teleport_dist
                    heapq.heappush(queue, (teleport_dist, teleport))

    return distance


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    print(dijkstra(n, k)[k])
