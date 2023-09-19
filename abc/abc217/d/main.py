import sys
from bisect import bisect_left
import array

sys.setrecursionlimit(10**9)


def main():
    L, Q = map(int, input().split())

    cutted = array.array("i", [0, L])
    for _ in range(Q):
        c, x = map(int, input().split())

        r = bisect_left(cutted, x)
        l = r - 1

        if c == 1:
            cutted.insert(r, x)
        else:
            print(cutted[r] - cutted[l])


if __name__ == "__main__":
    main()
