import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    pre = None
    l = None
    L = []
    R = []
    for i, a in enumerate(sorted(A)):
        if pre is None:
            pre = a
            l = a
        else:
            if a - pre > 1:
                L.append(l)
                R.append(pre)
                l = a
                pre = None
            else:
                pre = a
    else:
        if pre:
            L.append(l)
            R.append(pre)
        else:
            L.append(l)
            R.append(R)

    for _ in range(Q):
        i, x = map(int, input().split())


if __name__ == "__main__":
    main()
