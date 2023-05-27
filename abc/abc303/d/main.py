def main():
    X, Y, Z = map(int, input().split())
    S = input()

    dp = [[0, 0] for _ in range(len(S) + 1)]
    dp[0] = [Z, 0]
    for i, s in enumerate(S, 1):
        if s == "a":
            dp[i][0] = min(dp[i - 1][0] + Y, dp[i - 1][0] + Z + X + Z, dp[i - 1][1] + Z + X, dp[i - 1][1] + Y + Z)
            dp[i][1] = min(dp[i - 1][0] + Z + X, dp[i - 1][0] + Y + Z, dp[i - 1][1] + X, dp[i - 1][1] + Z + Y + Z)
        else:
            dp[i][0] = min(dp[i - 1][0] + X, dp[i - 1][0] + Z + Y + Z, dp[i - 1][1] + Z + X, dp[i - 1][1] + Y + Z)
            dp[i][1] = min(dp[i - 1][0] + X + Z, dp[i - 1][0] + Z + Y + Z,  dp[i - 1][1] + Y, dp[i - 1][1] + Z + X + Z)

    print(min(dp[len(S)]))


if __name__ == "__main__":
    main()
