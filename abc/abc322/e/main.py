import sys

sys.setrecursionlimit(10**9)


def main():
    N, K, P = map(int, input().split())
    C, A = [], []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    INF = float("inf")
    MAX = (P + 1) ** K
    dp = [[INF for _ in range(MAX)] for _ in range(N + 1)]
    dp[0][0] = 0
    for n in range(1, N + 1):
        cost = C[n - 1]

        for i in range((P + 1) ** K):
            if dp[n - 1][i] == INF:
                continue

            a = []
            ii = i
            for _ in range(K - 1, -1, -1):
                a.append(ii % (P + 1))
                ii //= P + 1

            a = a[::-1]

            dp[n][i] = min(dp[n][i], dp[n - 1][i])

            vv = 0
            for j, (ai, Ai) in enumerate(zip(a, A[n - 1])):
                vv += min(ai + Ai, P) * (P + 1) ** (K - j - 1)

            dp[n][vv] = min(dp[n][vv], dp[n - 1][i] + cost)

    print(dp[N][(P + 1) ** K - 1] if dp[N][(P + 1) ** K - 1] != INF else -1)


if __name__ == "__main__":
    main()
