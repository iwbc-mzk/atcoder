def main():
    N = int(input())

    dp = [[0] * 6 for _ in range(N + 1)]
    for n in range(1, N + 1):
        for v in range(6):
            dp[n][v] = max(v + 1, sum(dp[n - 1]) / 6)

    ans = sum(dp[N]) / 6
    print(ans)


if __name__ == "__main__":
    main()
