from test_framework import generic_test


def parity(x: int) -> int:
    result = 0
    while x > 0:
        result = result + 1 if x & 1 == 1 else result + 0
        x >>= 1
    return 1 if result % 2 != 0 else 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
