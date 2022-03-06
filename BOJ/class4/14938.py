# 예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다.
# 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다.
# 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다.
# 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는 낙하산에서 떨어질 때
# 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만 어디로 낙하해야
# 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.

# 각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다.
# 예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때,
# 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.

# # class 4+
import sys
import heapq
input = sys.stdin.readline


def floyd_warshall():
    global graph

    for come in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                graph[x][y] = min(graph[x][y], graph[x][come] + graph[come][y])


if __name__ == "__main__":
    n, m, r = map(int, input().strip().split())
    items = [0] + list(map(int, input().strip().split()))
    graph = [[sys.maxsize if i != j else 0 for i in range(
        n+1)] for j in range(n+1)]
    for _ in range(r):
        start, end, cost = map(int, input().strip().split())
        graph[start][end] = cost
        graph[end][start] = cost
    floyd_warshall()

    max_item = 0
    for x in range(1, n+1):
        item = 0
        for idx, dist in enumerate(graph[x]):
            if dist <= m:
                item += items[idx]

        max_item = max(max_item, item)
    print(max_item)
