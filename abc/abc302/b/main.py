def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                ans = []
                for k, s in enumerate("snuke"):
                    h, w = i + dh * k, j + dw * k
                    if not (0 <= h < H and 0 <= w < W):
                        break

                    if S[h][w] == s:
                        ans.append((h + 1, w + 1))
                        continue
                    else:
                        ans = []
                        break
                else:
                    for a in ans:
                        print(*a)



if __name__ == "__main__":
    main()