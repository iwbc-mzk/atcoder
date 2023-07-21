def main():
    N, L = map(int, input().split())

    MOD = 10**9 + 7

    dp = [0 for _ in range(N + 1)]
    dp[0] = 1

    for i in range(1, N + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1] % MOD
        if i - L >= 0:
            dp[i] += dp[i - L] % MOD

        dp[i] %= MOD

    print(dp[N])


if __name__ == "__main__":
    main()
