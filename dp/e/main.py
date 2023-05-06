from collections import defaultdict
import math

def main():
    N, W = map(int, input().split())

    dp = defaultdict(lambda: defaultdict(lambda: math.inf))
    dp[0][0] = 0
    for n in range(1, N + 1):
        wn, vn = map(int, input().split())
        for v in range(10 ** 5 + 1):
            if v - vn >= 0:
                dp[n][v] = min(dp[n - 1][v - vn] + wn, dp[n - 1][v])
            else:
                dp[n][v] = dp[n - 1][v]

    for v in reversed(range(len(dp[N]) + 1)):
        w = dp[N][v]
        if w <= W:
            print(v)
            break

if __name__ == "__main__":
    main()