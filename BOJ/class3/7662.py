# 이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다. 전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.

# 정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.

# Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
# class3+
import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        min_heap = []
        max_heap = []
        n = int(input())
        visited = [False for _ in range(n)]
        for i in range(n):
            order, n = map(str, input().strip().split())
            n = int(n)

            if order == "I":
                heapq.heappush(min_heap, (n, i))
                heapq.heappush(max_heap, (-n, i))
            else:
                if min_heap:
                    if n == 1:
                        while max_heap and visited[max_heap[0][1]]:
                            heapq.heappop(max_heap)
                        if max_heap:
                            visited[max_heap[0][1]] = True
                            heapq.heappop(max_heap)

                    else:
                        while min_heap and visited[min_heap[0][1]]:
                            heapq.heappop(min_heap)
                        if min_heap:
                            visited[min_heap[0][1]] = True
                            heapq.heappop(min_heap)

        while max_heap and visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        while min_heap and visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

        if min_heap and max_heap:
            print(
                f"{-heapq.heappop(max_heap)[0]} {heapq.heappop(min_heap)[0]}")
        else:
            print("EMPTY")
