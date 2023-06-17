def main():
    N = int(input())

    XY = []
    for _ in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))

    dp = [[0, 0] for _ in range(N + 1)]
    dp[0] = [0, 0]
    for i in range(1, N + 1):
        x, y = XY[i - 1]
        if x == 0:
            dp[i][0] = max(max(dp[i - 1]) + y, dp[i - 1][0])
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][0] + y, dp[i - 1][1])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
