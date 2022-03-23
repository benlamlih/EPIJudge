from test_framework import generic_test


def parity(x: int) -> int:
    # The complexity is O(k) with k is the number of 1s in x
    # Because by doing x &= x - 1 we drop the lowest set of bit x, so we drop the last 1
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
