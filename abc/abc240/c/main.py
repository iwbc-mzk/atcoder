import sys

sys.setrecursionlimit(10**9)


def main():
    N, X = map(int, input().split())

    dp = [[False] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for n in range(1, N + 1):
        a, b = map(int, input().split())
        for x in range(X + 1):
            if x - a >= 0 and dp[n - 1][x - a]:
                dp[n][x] = True
            if x - b >= 0 and dp[n - 1][x - b]:
                dp[n][x] = True

    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
