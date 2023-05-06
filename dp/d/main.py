from collections import defaultdict

def main():
    N, W = map(int, input().split())

    dp = defaultdict(lambda: defaultdict(int))
    for n in range(1, N + 1):
        wn, vn = map(int, input().split())
        for w in range(W + 1):
            if w - wn >= 0:
                dp[n][w] = max(dp[n - 1][w - wn] + vn, dp[n - 1][w])
            else:
                dp[n][w] = dp[n - 1][w]
    
    print(dp[N][W])


if __name__ == "__main__":
    main()