from collections import defaultdict

def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    dp = defaultdict(lambda: 10 ** 10)
    dp[1] = 0
    for n in range(1, N + 1):
        for k in range(1, K + 1):
            if n > k:
                dp[n] = min(dp[n], dp[n - k] + abs(H[n - 1] - H[n - 1 - k]))

    print(dp[N])


if __name__ == "__main__":
    main()