def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # dp[i][j] : 皿の上の飴の数がj(X mod N)個の時、そこから2^i回操作を繰り返すことで追加される飴の総数
    dp = [[0] * N for _ in range(41)]
    for i in range(N):
        dp[0][i] = A[i]

    for i in range(1, 41):
        for j in range(N):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][(j + dp[i - 1][j]) % N]

    ans = 0
    i = 0
    while K:
        if K & 1:
            ans += dp[i][ans % N]

        K >>= 1
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
