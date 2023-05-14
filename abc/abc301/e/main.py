def main():
    H, W, T = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    dp = [[[0] * T for _ in range(W)].copy() for _ in range(H)]
    for h in range(H):
        for w in range(W):
            a = A[h][w]
            if a == "#":
                continue

            c = 1 if a == "o" else 0
            for t in range(T):
                if h > 0:
                    dp[h][w][t] = max(dp[h][w][t], dp[h - 1][w][t - 1] + c)
                if h + 1 < H:
                    dp[h][w][t] = max(dp[h][w][t], dp[h + 1][w][t - 1] + c)
                if w > 0:
                    dp[h][w][t] = max(dp[h][w][t], dp[h][w - 1][t - 1] + c)
                if w + 1 < W:
                    dp[h][w][t] = max(dp[h][w][t], dp[h][w + 1][t - 1] + c)

    print(dp[H - 1][W - 1][T - 1])



if __name__ == "__main__":
    main()