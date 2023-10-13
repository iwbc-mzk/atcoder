def main():
    N, M, K = map(int, input().split())
    MOD = 998244353

    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0] = [1 for _ in range(M)]
    R = [0]
    for v in dp[0]:
        R.append(R[-1] + v)

    for n in range(1, N):
        NR = [0]
        for i in range(M):
            if K:
                if i + K <= M - 1:
                    dp[n][i] += R[-1] - R[i + K]
                if 0 <= i - K + 1:
                    dp[n][i] += R[i - K + 1]
            else:
                dp[n][i] += R[-1]

            dp[n][i] %= MOD
            NR.append(NR[-1] + dp[n][i])
        R = NR

    print(sum(dp[N - 1]) % MOD)


if __name__ == "__main__":
    main()
