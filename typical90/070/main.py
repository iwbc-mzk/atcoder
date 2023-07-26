def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    X, Y = [], []
    for x, y in XY:
        X.append(x)
        Y.append(y)

    X.sort()
    Y.sort()

    if N % 2:
        c = N // 2
        xmd = sum(abs(x - X[c]) for x in X)
        ymd = sum(abs(y - Y[c]) for y in Y)
    else:
        c = N // 2
        xavg = (X[c] + X[c - 1]) // 2
        yavg = (Y[c] + Y[c - 1]) // 2
        xmd = sum(abs(x - xavg) for x in X)
        ymd = sum(abs(y - yavg) for y in Y)

    print(xmd + ymd)


if __name__ == "__main__":
    main()
