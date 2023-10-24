def main():
    H, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    max_a = max(x[0] for x in AB)

    INF = float("inf")
    dp = [INF for _ in range(H + 1 + max_a)]
    dp[0] = 0
    for h in range(1, H + 1 + max_a):
        for n in range(N):
            a, b = AB[n]
            if h - a >= 0 and dp[h - a] != INF:
                dp[h] = min(dp[h], dp[h - a] + b)

    print(min(dp[H:]))


if __name__ == "__main__":
    main()
