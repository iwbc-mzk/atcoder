import bisect


def main():
    N, K = map(int, input().split())
    X = [*map(int, input().split())]

    i = bisect.bisect_left(X, 0)
    LX = sorted([*map(lambda x: -x, X[:i])])
    RX = X[i:]

    ans = float("inf")
    for l in range(K + 1):
        if l > len(LX):
            break

        r = K - l
        if r > len(RX):
            continue

        ld = LX[l - 1] if l != 0 else 0
        rd = RX[r - 1] if r != 0 else 0

        ans = min(ans, min(ld, rd) + ld + rd)

    print(ans)


if __name__ == "__main__":
    main()
