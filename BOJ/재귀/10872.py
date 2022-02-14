# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input())

    print(factorial(n))