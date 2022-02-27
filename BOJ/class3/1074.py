# Z
# class 3+
import sys
input = sys.stdin.readline


def Z(n, r, c):
    if n == 1:
        return 2 * r + c

    half = 2 ** (n-1)
    if r < half and c < half:
        section = 1
    elif r < half and c >= half:
        section = 2
        c -= half
    elif r >= half and c < half:
        section = 3
        r -= half
    else:
        section = 4
        r -= half
        c -= half

    return Z(n-1, r, c) + half ** 2 * (section - 1)


if __name__ == "__main__":
    n, r, c = map(int, input().strip().split())

    print(Z(n, r, c))
