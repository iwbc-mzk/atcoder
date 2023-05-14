def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    dp = [[-1, -1, -1] for _ in range(N + 1)]
    dp[0] = 0, 0, 0
    for i, t in enumerate(T, 1):
        if i <= K:
            if t == "r":
                dp[i] = max(dp[i - 1]), max(dp[i - 1]), max(dp[i - 1]) + R
            if t == "s":
                dp[i] = max(dp[i - 1]) + S, max(dp[i - 1]), max(dp[i - 1])
            if t == "p":
                dp[i] = max(dp[i - 1]), max(dp[i - 1]) + P, max(dp[i - 1])


if __name__ == "__main__":
    main()