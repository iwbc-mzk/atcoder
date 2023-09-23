import sys

sys.setrecursionlimit(10**9)


def main():
    K = int(input())

    L = []

    def rec(v):
        nonlocal L
        L.append(v)
        l = v % 10
        vv = v * 10
        for i in range(l):
            rec(vv + i)

    for i in range(1, 10):
        rec(i)

    L.sort()

    print(L[K - 1])


if __name__ == "__main__":
    main()
