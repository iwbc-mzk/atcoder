import sys
from functools import cache

sys.setrecursionlimit(10**9)


@cache
def fib(k):
    if k in [0, 1]:
        return 1

    return fib(k - 1) + fib(k - 2)


def main():
    K = int(input())

    a = fib(K + 1)
    b = fib(K)
    print(a, b)


if __name__ == "__main__":
    main()
