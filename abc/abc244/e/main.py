def main():
    N, M, K, S, T, X = map(int, input().split())

    MOD = 998244353

    UV = []
    for _ in range(M):
        U, V = map(int, input().split())
        UV.append((U, V))

    dp = [[[0, 0] for _ in range(N + 1)] for _ in range(K + 1)]
    dp[0][S][1] = 1

    def calc(dp, k, from_, to_):
        if to_ == X:
            dp[k][to_][0] += dp[k - 1][from_][1]
            dp[k][to_][1] += dp[k - 1][from_][0]
        else:
            dp[k][to_][0] += dp[k - 1][from_][0]
            dp[k][to_][1] += dp[k - 1][from_][1]

        dp[k][to_][0] %= MOD
        dp[k][to_][1] %= MOD

    for k in range(1, K + 1):
        for u, v in UV:
            calc(dp, k, u, v)
            calc(dp, k, v, u)

    print(dp[K][T][1])


if __name__ == "__main__":
    main()
