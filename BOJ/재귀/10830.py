# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 분할 정복
import sys
input = sys.stdin.readline


def matrix_mul(matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for i in range(n):
                result[x][y] += matrix1[x][i] * matrix2[i][y]
            result[x][y] %= 1000
    return result


def matrix_square(matrix):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for i in range(n):
                result[x][y] += matrix[x][i] * matrix[i][y]
            result[x][y] %= 1000
    return result


def divide(matrix, n):
    if n == 1:
        return matrix

    if n == 2:
        return matrix_square(matrix)

    if n % 2 == 0:
        return matrix_square(divide(matrix, n // 2))

    return matrix_mul(matrix_square(divide(matrix, n//2)), matrix)


if __name__ == "__main__":
    n, b = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]

    for line in divide(matrix, b):
        for data in line:
            print(data % 1000, end=" ")
        print()
