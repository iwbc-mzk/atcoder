def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    R = [a % D for a in A]
    dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for k in range(K + 1):
            for j in range(D):
                t = (j - R[i - 1] + D) % D
                if k - 1 >= 0 and dp[i - 1][k - 1][t] >= 0:
                    dp[i][k][j] = max(
                        dp[i][k][j], dp[i - 1][k - 1][(j - R[i - 1] + D) % D] + A[i - 1]
                    )
                if dp[i - 1][k][j] >= 0:
                    dp[i][k][j] = max(dp[i][k][j], dp[i - 1][k][j])

    print(dp[N][K][0])


if __name__ == "__main__":
    main()
