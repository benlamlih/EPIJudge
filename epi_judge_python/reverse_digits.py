from test_framework import generic_test


def reverse(x: int) -> int:
    # -314  -> 413
    # 42 -> 24
    neg = False
    if x < 0:
        x = -x
        neg = True
    res = 0
    while x:
        res *= 10
        res += x % 10
        x //= 10

    return -res if neg else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))