# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
# class 3++
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        P = input().strip()
        n = int(input())
        num_list = input().strip()[1:-1].split(",")
        if num_list[0] == "":
            num_list = []

        R_num = 0
        check = True
        for p in P:
            if p == "R":
                R_num += 1
            else:
                if num_list:
                    if R_num % 2 == 0:
                        num_list.pop(0)
                    else:
                        num_list.pop(-1)
                else:
                    print("error")
                    check = False
                    break

        if check:
            if R_num % 2 != 0:
                num_list.reverse()

            print("[" + ",".join(num_list) + "]")
