import sys
from math import ceil

sys.setrecursionlimit(10**9)


def main():
    N, a, b = map(int, input().split())
    A = list(map(int, input().split()))

    avg = sum(A) // N
    l, r = 0, avg + 1
    while r - l > 1:
        m = (l + r) // 2

        up, down = 0, 0
        for ai in A:
            if ai < m:
                up += ceil((m - ai) / a)
            else:
                down += (ai - m) // b

        if down >= up:
            l = m
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main()
