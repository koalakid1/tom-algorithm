# 때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
# (단 도로는 방향이 없으며 웜홀은 방향이 있다.)
# 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
# 웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

# 시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
# 한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
# 여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.
# # class 4
import sys
import heapq
input = sys.stdin.readline


def bellman_fold(graph, start):
    distance = [sys.maxsize for _ in range(n+1)]

    distance[start] = 0

    for _ in range(n-1):
        for node in range(1, n+1):
            for next_node, cost in graph[node]:
                next_distance = distance[node] + cost
                if distance[next_node] > next_distance:
                    distance[next_node] = next_distance

    for node in range(1, n+1):
        for next_node, cost in graph[node]:
            next_distance = distance[node] + cost
            if distance[next_node] > next_distance:
                return 1
    return 0


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, w = map(int, input().strip().split())

        roads = [[] for _ in range(n+1)]
        # worms = [[] for _ in range(n+1)]
        for _ in range(m):
            s, e, t = map(int, input().strip().split())
            roads[s].append((e, t))
            roads[e].append((s, t))

        for _ in range(w):
            s, e, t = map(int, input().strip().split())
            roads[s].append((e, -t))

        if bellman_fold(roads, 1):
            print("YES")
        else:
            print("NO")
