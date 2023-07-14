def main():
    MOD = 10**9 + 7

    N = int(input())
    S = input()

    DP = [[0 for _ in range(len("atcoder") + 1)] for _ in range(N + 1)]
    DP[0][0] = 1
    for i, s in enumerate(S, 1):
        for j, si in enumerate(" atcoder"):
            if s == si:
                DP[i][j] += DP[i - 1][j - 1] % MOD

            DP[i][j] += DP[i - 1][j] % MOD
            DP[i][j] = DP[i][j] % MOD

    print(DP[N][7])


if __name__ == "__main__":
    main()
