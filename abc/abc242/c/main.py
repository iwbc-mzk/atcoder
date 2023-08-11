import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    MOD = 998244353

    dp = [[0] * 9 for _ in range(N)]
    dp[0] = [1] * 9

    for n in range(N):
        for i in range(9):
            dp[n][i] += dp[n - 1][i]
            if i == 0:
                dp[n][i] += dp[n - 1][i + 1]
            elif i == 8:
                dp[n][i] += dp[n - 1][i - 1]
            else:
                dp[n][i] += dp[n - 1][i - 1] + dp[n - 1][i + 1]

            dp[n][i] %= MOD

    print(sum(dp[N - 1]) % MOD)


if __name__ == "__main__":
    main()
