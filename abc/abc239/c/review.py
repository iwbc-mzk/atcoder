def main():
    x1, y1, x2, y2 = map(int, input().split())

    for dx, dy in [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]:
        xx, yy = x1 + dx, y1 + dy

        if (x2 - xx) ** 2 + (y2 - yy) ** 2 == 5:
            print("Yes")
            return
    else:
        print("No")


if __name__ == "__main__":
    main()
