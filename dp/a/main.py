from collections import defaultdict

def main():
    N = int(input())
    H = list(map(int, input().split()))

    dp = defaultdict(lambda: 10 ** 10)
    dp[1] = 0
    for n in range(1, N + 1):
        if n > 1:
            dp[n] = min(dp[n], dp[n - 1] + abs(H[n - 1] - H[n - 2]))

        if n > 2:
            dp[n] = min(dp[n], dp[n - 2] + abs(H[n - 1] - H[n - 3]))

    print(dp[N])


if __name__ == "__main__":
    main()