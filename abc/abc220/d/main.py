def main():
    N = int(input())
    A = list(map(int, input().split()))

    MOD = 998244353

    dp = [[0 for _ in range(10)] for _ in range(N)]
    dp[0][A[0]] = 1
    for i in range(1, N):
        for k in range(10):
            t = k + A[i] % 10
            t %= 10
            dp[i][t] += dp[i - 1][k] % MOD
            dp[i][t] %= MOD

            t = k * (A[i] % 10)
            t %= 10
            dp[i][t] += dp[i - 1][k] % MOD
            dp[i][t] %= MOD
    
    ans = dp[N - 1]
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()