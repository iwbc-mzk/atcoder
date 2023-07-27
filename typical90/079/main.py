def main():
    H, W = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    AB = []
    for a, b in zip(A, B):
        ab = []
        for ai, bi in zip(a, b):
            ab.append(bi - ai)
        AB.append(ab)

    cnt = 0
    for x in range(H - 1):
        for y in range(W - 1):
            v = AB[x][y]
            for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                xx, yy = x + dx, y + dy
                AB[xx][yy] -= v
            cnt += abs(v)

    result = sum(sum(ab) for ab in AB)
    if result == 0:
        print("Yes")
        print(cnt)
    else:
        print("No")


if __name__ == "__main__":
    main()
