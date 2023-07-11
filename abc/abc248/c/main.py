def main():
    N, M, K = map(int, input().split())

    MOD = 998244353

    DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    DP[0][0] = 1

    for n in range(1, N + 1):
        for k in range(1, K + 1):
            for m in range(1, M + 1):
                if k - m >= 0:
                    DP[n][k] += DP[n - 1][k - m] % MOD
                    DP[n][k] %= MOD

    print(sum(DP[N]) % MOD)


if __name__ == "__main__":
    main()
