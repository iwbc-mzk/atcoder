from collections import defaultdict


def main():
    N = int(input())

    max_t = 0
    TXA = defaultdict(int)
    for _ in range(N):
        t, x, a = map(int, input().split())
        TXA[(t, x)] = a
        max_t = max(max_t, t)

    dp = [[-1 for _ in range(5)] for _ in range(max_t + 1)]
    dp[0][0] = 0

    for t in range(1, max_t + 1):
        for h in range(5):
            if (t, h) in TXA:
                s = TXA[(t, h)]
            else:
                s = 0

            if dp[t - 1][h] != -1:
                dp[t][h] = max(dp[t][h], dp[t - 1][h] + s)
            if h - 1 >= 0 and dp[t - 1][h - 1] != -1:
                dp[t][h] = max(dp[t][h], dp[t - 1][h - 1] + s)
            if h + 1 <= 4 and dp[t - 1][h + 1] != -1:
                dp[t][h] = max(dp[t][h], dp[t - 1][h + 1] + s)

    print(max(dp[max_t]))


if __name__ == "__main__":
    main()
