def main():
    N = int(input())
    A = list(map(int, input().split()))

    MOD = 998244353

    ans = 0

    for n in range(1, N + 1):
        dp = [[[0] * n for _ in range(N + 1)] for _ in range(N + 1)]
        dp[0][0][0] = 1

        for i in range(N):
            for j in range(i + 1):
                for k in range(n):
                    # Aのi番目を追加しない
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD

                    # Aのi番目を追加する
                    dp[i + 1][j + 1][(k + A[i]) % n] += dp[i][j][k]
                    dp[i + 1][j + 1][(k + A[i]) % n] %= MOD

        ans += dp[N][n][0]
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
