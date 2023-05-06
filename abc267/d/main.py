from collections import defaultdict
import math

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # dp[n][m]: A1~Ai列から長さMの部分列に対する最大値
    dp = defaultdict(lambda: defaultdict(lambda: -math.inf))
    for n in range(N + 1):
        for m in range(n + 1):
            if n == 0 or m == 0:
                dp[n][m] = 0
            else:
                dp[n][m] = max(dp[n - 1][m], dp[n - 1][m - 1] + A[n - 1] * m)


    print(dp[N][M])

if __name__ == "__main__":
    main()