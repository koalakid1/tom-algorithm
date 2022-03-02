# 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
# 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다.
# 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

# class 3++
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        clothes = {}
        for _ in range(int(input())):
            clothes_name, clothes_type = map(str, input().strip().split())
            if clothes_type in clothes:
                clothes[clothes_type].append(clothes_name)
            else:
                clothes[clothes_type] = [clothes_name]

        ans = 1
        for clothes_type in clothes:
            ans *= len(clothes[clothes_type]) + 1

        print(ans - 1)
