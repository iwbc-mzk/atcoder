def main():
    N, M, K = map(int, input().split())
    MOD = 998244353

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for n in range(1, N + 1):
        for k in range(K + 1):
            for m in range(1, M + 1):
                if not (0 <= k - m <= K):
                    continue

                dp[n][k] += dp[n - 1][k - m]
                dp[n][k] %= MOD

    print(sum(dp[N]) % MOD)


if __name__ == "__main__":
    main()
