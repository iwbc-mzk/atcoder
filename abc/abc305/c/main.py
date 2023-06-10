def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for h in range(H):
        for w in range(W):
            cnt = 0
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                hh = h + x
                ww = w + y
                if 0 <= hh < H and 0 <= ww < W:
                    if S[h][w] != "#" and S[hh][ww] == "#":
                        cnt += 1
            else:
                if cnt >= 2:
                    print(h + 1, w + 1)
                    return


if __name__ == "__main__":
    main()
