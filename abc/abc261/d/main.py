def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = {}
    for _ in range(M):
        c, y = map(int, input().split())
        CY[c] = y

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(N + 1):
            if j == 0:
                dp[i][0] = max(dp[i - 1])
            else:
                if dp[i - 1][j - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
                    if j in CY:
                        dp[i][j] += CY[j]

    print(max(dp[N]))


if __name__ == "__main__":
    main()
