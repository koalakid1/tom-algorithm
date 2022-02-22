# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# class2+

import sys
input = sys.stdin.readline


def 최대공약수(num1, num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


def 최소공배수(num1, num2):
    return (num1 * num2) // 최대공약수(num1, num2)


if __name__ == "__main__":
    num1, num2 = map(int, input().strip().split())

    print(최대공약수(num1, num2))
    print(최소공배수(num1, num2))
