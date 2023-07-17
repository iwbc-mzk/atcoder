def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        print(H * W)
        return

    ans = 0
    for sh in [0, 1]:
        for sw in [0, 1]:
            if not (0 <= sh < H and 0 <= sw < W):
                continue

            R = [[0 for _ in range(W)] for _ in range(H)]
            R[sh][sw] = 1
            for dh in [0, 1, -1]:
                for dw in [0, 1, -1]:
                    if 0 <= sh + dh < H and 0 <= sw + dw < W:
                        R[sh + dh][sw + dw] = -1

            cnt = 1
            for h in range(H):
                for w in range(W):
                    if R[h][w] == 0:
                        R[h][w] = 1
                        cnt += 1

                        for dh in [0, 1, -1]:
                            for dw in [0, 1, -1]:
                                if 0 <= h + dh < H and 0 <= w + dw < W:
                                    R[h + dh][w + dw] = -1

            ans = max(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
