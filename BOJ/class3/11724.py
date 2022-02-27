# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# class3+
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    graph_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        graph_list[u].append(v)
        graph_list[v].append(u)

    ans = 0
    check = [True for _ in range(n+1)]
    for idx in range(1, n+1):
        if check[idx]:
            queue = [idx]
            check[idx] = False
            while queue:
                u = queue.pop(0)
                for v in graph_list[u]:
                    if check[v]:
                        queue.append(v)
                        check[v] = False

            ans += 1
    print(ans)
