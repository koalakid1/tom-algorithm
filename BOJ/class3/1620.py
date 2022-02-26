# 나는야 포켓몬마스터 이다솜
# class3+
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    포켓몬리스트 = [input().strip() for _ in range(n)]

    for _ in range(m):
        문제 = input().strip()
        if 문제.isdigit():
            print(포켓몬리스트[int(문제)-1])
        else:
            print(포켓몬리스트.index(문제)+1)
