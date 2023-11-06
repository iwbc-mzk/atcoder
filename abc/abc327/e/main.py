import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    P = list(map(int, input().split()))

    dp = [[(None, None) for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = (0, 0)
    for n in range(1, N + 1):
        for j in range(N + 1):
            dp[n][j] = dp[n - 1][j]
            if j > 0:
                vjt, vjb = dp[n - 1][j - 1]
                if vjt is None and vjb is None:
                    continue

                vt = vjt * 0.9 + P[n - 1]
                vb = vjb * 0.9 + 1

                if dp[n][j] == (None, None):
                    dp[n][j] = (vt, vb)
                elif (dp[n][j][0] / dp[n][j][1] - 1200 / (j**0.5)) < (
                    vt / vb - 1200 / ((j**0.5))
                ):
                    dp[n][j] = (vt, vb)

    ans = None
    for i, (t, b) in enumerate(dp[N]):
        if not b:
            continue

        if not ans:
            ans = t / b - 1200 / (i**0.5)
        else:
            ans = max(ans, t / b - 1200 / (i**0.5))

    print(ans)


if __name__ == "__main__":
    main()
    # 940.96
