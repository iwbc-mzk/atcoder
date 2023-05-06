def main():
    N, M = map(int, input().split())
    A = set(int(input()) for _ in range(M))

    dp = [0] * (N+1)
    for n in range(N+1):
        if n == 0:
            dp[0] = 1

        if n in A:
            continue

        if n >= 1 and dp[n-1] > 0:
            dp[n] += dp[n-1]
        if n >= 2 and dp[n-2] > 0:
            dp[n] += dp[n-2]

    print(dp[N] % 1000000007)

if __name__ == "__main__":
    main()