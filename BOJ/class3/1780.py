# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# class3++

import sys
input = sys.stdin.readline


def paper_num(x, y, n):
    global negative, zero, positive

    check = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        paper_num(x+k * n//3, y + l * n//3, n//3)
                return

    if check == -1:
        negative += 1
    elif check == 0:
        zero += 1
    else:
        positive += 1


if __name__ == "__main__":
    n = int(input())

    graph = [list(map(int, input().strip().split())) for _ in range(n)]

    negative = 0
    zero = 0
    positive = 0

    paper_num(0, 0, n)

    print(f"{negative}\n{zero}\n{positive}")
