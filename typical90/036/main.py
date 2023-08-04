def main():
    N, Q = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    RXY = []
    minx, maxx, miny, maxy = float("inf"), -float("inf"), float("inf"), -float("inf")
    for x, y in XY:
        x, y = x + y, x - y
        RXY.append((x, y))
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)

    for _ in range(Q):
        q = int(input())
        x, y = RXY[q - 1]
        print(max(abs(x - minx), abs(x - maxx), abs(y - miny), abs(y - maxy)))


if __name__ == "__main__":
    main()
