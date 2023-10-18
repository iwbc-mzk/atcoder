def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    max_x, min_x, max_y, min_y = (
        -float("inf"),
        float("inf"),
        -float("inf"),
        float("inf"),
    )
    for x, y in XY:
        xx, yy = x + y, x - y
        max_x = max(max_x, xx)
        min_x = min(min_x, xx)
        max_y = max(max_y, yy)
        min_y = min(min_y, yy)

    print(max(max_x - min_x, max_y - min_y))


if __name__ == "__main__":
    main()
