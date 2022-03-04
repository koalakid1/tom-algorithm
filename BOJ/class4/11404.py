# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.

# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
# # class 4+
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    city_num = int(input())
    bus_num = int(input())
    graph = [[sys.maxsize for _ in range(city_num+1)]
             for _ in range(city_num+1)]
    for _ in range(bus_num):
        start, end, cost = map(int, input().strip().split())
        graph[start][end] = min(graph[start][end], cost)

    for visit_city in range(1, city_num+1):
        for x in range(1, city_num+1):
            for y in range(1, city_num+1):
                now_cost = graph[x][visit_city] + graph[visit_city][y]
                if x != y and graph[x][y] > now_cost:
                    graph[x][y] = now_cost

    for x in range(1, city_num+1):
        for y in range(1, city_num+1):
            if graph[x][y] == sys.maxsize:
                print(0, end=" ")
            else:
                print(graph[x][y], end=" ")
        print()

    print(*graph)
