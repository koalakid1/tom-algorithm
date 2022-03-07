# 시그마

# # class 4+
from math import gcd
import sys
input = sys.stdin.readline


def power(n, x):
    if x == 1:
        return n

    if x == 2:
        return (n * n) % mod

    temp = power(n, x//2)

    if x % 2 == 0:
        return (temp * temp) % mod

    return (n * (temp * temp) % mod) % mod


if __name__ == "__main__":
    mod = 1000000007
    m = int(input())
    ans = 0
    for _ in range(m):
        n, s = map(int, input().strip().split())
        g = gcd(n, s)
        n //= g
        s //= g
        ans += s * power(n, mod-2)
        ans %= mod
    print(ans)
