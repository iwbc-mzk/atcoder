import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    m = 0
    mi = -1
    c = [0] * (N + 1)
    for i, a in enumerate(A):
        c[a] += 1
        if c[a] > m:
            m = c[a]
            mi = a
        elif c[a] == m and a < mi:
            m = c[a]
            mi = a

        print(mi)


if __name__ == "__main__":
    main()
