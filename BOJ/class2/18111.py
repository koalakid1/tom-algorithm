# 마인크래프트
# class2++

import sys
input = sys.stdin.readline


def 마인크래프트(n, m, b, 리스트):
    ans = sys.maxsize
    for height in range(257):
        빼내기 = 0
        놓기 = 0
        아이템 = b
        for x in range(n):
            for y in range(m):
                현재높이 = 리스트[x][y]
                if 현재높이 > height:
                    빼내기 += 현재높이 - height
                else:
                    놓기 += height - 현재높이
        아이템 += 빼내기
        if 아이템 >= 놓기:
            time = 빼내기 * 2 + 놓기
            if time <= ans:
                ans = time
                높이 = height

    return [ans, 높이]


if __name__ == "__main__":
    n, m, b = map(int, input().strip().split())
    리스트 = [list(map(int, input().strip().split())) for _ in range(n)]

    print(" ".join(map(str, 마인크래프트(n, m, b, 리스트))))
