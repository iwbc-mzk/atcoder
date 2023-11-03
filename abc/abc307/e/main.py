def main():
    N, M = map(int, input().split())
    MOD = 998244353

    dp = [[0, 0] for _ in range(N + 1)]
    for n in range(1, N + 1):
        if n == 1:
            dp[n][1] = M
        else:
            dp[n][0] += dp[n - 1][0] * (M - 2) + dp[n - 1][1] * (M - 1)
            dp[n][1] += dp[n - 1][0]

        dp[n][0] %= MOD
        dp[n][1] %= MOD

    print(dp[N][0])


if __name__ == "__main__":
    main()
