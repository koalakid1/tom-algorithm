def k_base(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base = str(mod) + rev_base
    return rev_base


def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    n = k_base(n, k)

    return m
