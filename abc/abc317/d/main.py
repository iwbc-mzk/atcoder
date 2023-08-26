import sys
import math

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    X, Y, Z = [], [], []
    for _ in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)

    total_z = sum(Z)

    dp = [[float("inf")] * (total_z + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for n in range(1, N + 1):
        for z in range(total_z + 1):
            if X[n - 1] > Y[n - 1]:
                if z - Z[n - 1] >= 0:
                    dp[n][z] = min(dp[n][z], dp[n - 1][z - Z[n - 1]])
            else:
                if z - Z[n - 1] >= 0:
                    dp[n][z] = min(
                        dp[n][z],
                        dp[n - 1][z - Z[n - 1]] + math.ceil((Y[n - 1] - X[n - 1]) / 2),
                    )
                dp[n][z] = min(dp[n][z], dp[n - 1][z])

    ans = float("inf")
    for z in range(math.ceil(total_z / 2), total_z + 1):
        ans = min(ans, dp[N][z])

    print(ans)


if __name__ == "__main__":
    main()
