def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    ans = 0
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        r, c = R + dx, C + dy
        if 1 <= r <= H:
            if 1 <= c <= W:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
