# 뱀과 사다리 게임을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

# 주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

# 게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다. 게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

# 플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. 예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다. 즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

# 게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

# 게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.
# class3++
import sys
from collections import deque
input = sys.stdin.readline


def bfs(ladder, snake):
    visited = [0 for _ in range(101)]
    queue = deque([1])

    while queue:
        num = queue.popleft()
        for dice in range(1, 7):
            next_num = num + dice
            if 0 < next_num <= 100:
                while True:
                    if not visited[next_num]:
                        visited[next_num] = visited[num] + 1
                        if next_num in ladder:
                            next_num = ladder[next_num]
                        elif next_num in snake:
                            next_num = snake[next_num]
                        else:
                            queue.append(next_num)
                            break
                    else:
                        break
    return visited[100]


if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    ladder, snake = {}, {}
    for _ in range(n):
        x, y = map(int, input().strip().split())
        ladder[x] = y

    for _ in range(m):
        u, v = map(int, input().strip().split())
        snake[u] = v

    print(bfs(ladder, snake))
