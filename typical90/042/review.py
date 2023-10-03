def main():
    K = int(input())
    MOD = 10**9 + 7

    if K % 9:
        print(0)
        return

    dp = [0 for _ in range(K + 1)]
    dp[0] = 1
    for i in range(1, K + 1):
        for j in range(1, 10):
            if i - j >= 0:
                dp[i] += dp[i - j] % MOD
                dp[i] %= MOD

    print(dp[K])


if __name__ == "__main__":
    main()
