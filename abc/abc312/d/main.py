import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    MOD = 998244353

    dp = [[0 for _ in range(len(S) + 1)] for _ in range(len(S) + 1)]
    dp[0][0] = 1

    for i, s in enumerate(S, 1):
        for j in range(len(S) + 1):
            if s == "(":
                if j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1]
            elif s == ")":
                if j + 1 <= len(S):
                    dp[i][j] = dp[i - 1][j + 1]
            else:
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1] % MOD
                if j + 1 <= len(S):
                    dp[i][j] += dp[i - 1][j + 1] % MOD

            dp[i][j] %= MOD

    print(dp[len(S)][0])


if __name__ == "__main__":
    main()
