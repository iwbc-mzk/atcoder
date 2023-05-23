def main():
    N = int(input())
    XY = list(tuple(map(int, input().split())) for _ in range(N))
    XY_set = set(XY)
    XY.sort(key=lambda x: x[0] * 10 + x[1])
    y_list = set(xy[1] for xy in XY)

    ans = 0
    for i in range(N):
        x1, y1 = XY[i]
        for j in range(i + 1, N):
            x2, y2 = XY[j]
            if not (x1 != x2 and y1 == y2):
                continue

            for y in y_list:
                if y <= y1:
                    continue

                if (x1, y) in XY_set and (x2, y) in XY_set:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
