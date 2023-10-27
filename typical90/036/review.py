def main():
    N, Q = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    XY = [(x + y, x - y) for x, y in XY]

    max_x = max(x[0] for x in XY)
    min_x = min(x[0] for x in XY)
    max_y = max(x[1] for x in XY)
    min_y = min(x[1] for x in XY)

    for _ in range(Q):
        q = int(input())
        px, py = XY[q - 1]
        print(max(abs(px - max_x), abs(px - min_x), abs(py - max_y), abs(py - min_y)))


if __name__ == "__main__":
    main()
