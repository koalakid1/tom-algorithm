# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
# # class 4+
import sys
input = sys.stdin.readline


def matrix_mul(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for i in range(n):
                result[x][y] += matrix1[x][i] * matrix2[i][y]
            result[x][y] %= 1000000007
    return result


def matrix_square(n, matrix):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for i in range(n):
                result[x][y] += matrix[x][i] * matrix[i][y]
            result[x][y] %= 1000000007
    return result


def matrix_power(matrix, n):
    if n == 1:
        return matrix

    if n == 2:
        return matrix_square(2, matrix)

    if n % 2 == 0:
        return matrix_square(2, matrix_power(matrix, n // 2))

    return matrix_mul(2, matrix_square(2, matrix_power(matrix, n//2)), matrix)


if __name__ == "__main__":
    n = int(input())
    matrix = [[1, 1], [1, 0]]
    matrix = matrix_power(matrix, n)

    print(matrix[0][1] % 1000000007)
