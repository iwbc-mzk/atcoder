import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [None] * (M + 1)

    for i, c in enumerate(C):
        for j in range(N, -1, -1):
            if j > i:
                continue

            a = A[j]
            bi = i - j
            if bi > M:
                break
            if B[bi] is not None:
                c -= a * B[bi]
            else:
                if a != 0:
                    B[bi] = c // a

    print(*B)


if __name__ == "__main__":
    main()
