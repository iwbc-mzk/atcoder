from collections import defaultdict


def main():
    N, X, Y = map(int, input().split())

    R = defaultdict(int)
    B = defaultdict(int)
    R[N] = 1
    for n in reversed(range(2, N + 1)):
        if n in R:
            R[n - 1] += R[n]
            B[n] += R[n] * X
        if n in B:
            R[n - 1] += B[n]
            B[n - 1] += B[n] * Y

    print(B[1])


if __name__ == "__main__":
    main()
